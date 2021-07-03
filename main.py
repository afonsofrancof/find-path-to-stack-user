from concurrent.futures import ThreadPoolExecutor
import json
import sys
import requests

level_list = {}


def checker():
    if len(sys.argv) < 3:
        print("Not enought arguments")
        raise SystemExit
    else:
        if len(sys.argv) > 3:
            print("Too many arguments provided")
            raise SystemExit
        else:
            test = requests.get(
                "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
                + sys.argv[2] + "&steamids= = "
                + sys.argv[1])
            test_json = json.loads(test.text)
            if len(test_json['response'].get('players', 0)) < 1:
                print("Invalid User ID or Invalid API KEY")
            else:
                print("Finding path from user:" + sys.argv[1])
                crawler(sys.argv[1])


def add_to_level_dict(user_id):
    level_list[user_id] = int(json.loads(
        requests.get("https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key="
                     + sys.argv[2] + "&steamid="
                     + str(user_id)).text)['response'].get('player_level', 0))
    return 0


def crawler(source_user_id):
    level_list.clear()
    if source_user_id == 76561198023414915:
        print("Found Stack's profile")
        raise SystemExit
    req = requests.get(
        url="https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + sys.argv[2] + "&steamid=" +
            str(source_user_id) + "&relationship=friend")
    req_json = json.loads(req.text)
    friends_list = req_json['friendslist']['friends']

    if len(friends_list) < 1:
        raise SystemExit
    with ThreadPoolExecutor(max_workers=2000) as executor:
        for friend in friends_list:
            if int(friend.get('steamid', 0)) == 76561198023414915:
                print("Found Stack's profile")
                raise SystemExit
            else:
                executor.submit(add_to_level_dict, int(friend.get('steamid', 0)))
    max_friend = max(level_list, key=lambda k: level_list[k])
    print(max_friend)
    crawler(max_friend)


checker()
