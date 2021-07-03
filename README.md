# St4ck steam profile finder

##Description
   An app that goes through a given friends list , finds the highest level friend,
   and does a recursive on that friend until it finds st4cks steam profile. Prints the pack along the way.

##Usage
**First generate a steam api key in https://steamcommunity.com/dev/apikey**

    python3 main.py [steam_user_id_64] [Steam_web_api_key]

##Bugs 
The programm still doesn't account for loops (2 people are each others highest level friend) and when someone has
private friend list.

These will probably be fixed in the future.
