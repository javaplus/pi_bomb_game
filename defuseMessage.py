import random


def getDefuseFailureMessage():

    dataList = [{ "say":"Bomb defusal failure! Bomb defusal failure! Lock out for 15 seconds", "parms" : "-s 140 -ven-us+f3"},
    { "say":"You are even more dumb than I first computed! You have 15 seconds to ask someone smarter for help.", "parms" : "-s 90 -ven-us+f3"},
    { "say":"That does not even come close to computing. Recalculate for the next 15 seconds", "parms" : "-s 90 -ven-us+f3"},
    { "say":"Do you always make such poor life choices.  Now ponder your failure for 15 seconds", "parms" : "-s 90 -ven-us+f3"}]

    random.choice(dataList)