import random


def getDefuseFailureMessage():

    dataList = [
    { "say":"You are even more dumb than I first computed! 15 seconds to retry.", "parms" : "-s 130 -ven-us+f3"},
    { "say":"That does not even come close to computing. Recalculate for the next 15 seconds", "parms" : "-s 130 -ven-us+f3"},
    { "say":"Do you always make such poor life choices.  Now ponder your failure for 15 seconds", "parms" : "-s 130 -ven-us+f3"},
    { "say":"Failure! There are only 4 buttons the odds are in your favor. Try harder in 15 seconds", "parms" : "-s 130 -ven-us+f3"}]

    message = random.choice(dataList)

    # print("message=" + message)

    return message
