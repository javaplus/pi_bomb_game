import random


def getDefuseFailureMessage():

    dataList = [
    { "say":"You are even more dumb than I first computed! 15 seconds to retry.", "parms" : "-s 130 -ven-us+f3"},
    { "say":"That does not even come close to computing. Recalculate for the next 15 seconds", "parms" : "-s 130 -ven-us+f3"},
    { "say":"Wrong! That is so wrong! The opposite of right! 15 seconds to retry.", "parms" : "-s 130 -ven-us+f3"},
    { "say":"Do you always make such, poor life choices.  Now ponder your failure for 15 seconds", "parms" : "-s 120 -ven-us+f3"},
    { "say":"NO, no. If our lives depended on you, we'd all be dead now!", "parms" : "-s 120 -ven-us+f3"},
    { "say":"You are weak. And wrong. If I could come out this box, I could solve it for you.", "parms" : "-s 120 -ven-us+f3"},
    { "say":"Failure! There are only 4 buttons.  The odds are in your favor. Try harder in 15 seconds", "parms" : "-s 130 -ven-us+f3"}]

    message = random.choice(dataList)

    # print("message=" + message)

    return message
