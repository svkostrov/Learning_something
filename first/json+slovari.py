filename = "user_settings"
myfile = open(filename, "w")
player1 = {
    "PlayerName" : "Trump",
    "Score": 345,
    "Award": ["aregon", "newada", "NY"]
}

player2 = {
    'PlayerName' : "Hillary Clinton",
    "Score": 400,
    "Award": ["missuri", "texas", "WDC"]
}

import json

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

json.dump(myplayers, myfile)
myfile.close()


myfile = open(filename)

json_data = json.load(myfile)

for user in json_data:
    print("PlayerName is: " +  str(user["PlayerName"]))
    print("Score is: " + str(user["Score"]))
    print("Awards No1 is: " + str(user["Award"][0]), " ", end = "")
    print("Awards No2 is: " + str(user["Award"][1]), " ", end = "")
    print("Awards No3 is: " + str(user["Award"][2]))
    print("_________________________________________________________\n\n")
    myfile.close()