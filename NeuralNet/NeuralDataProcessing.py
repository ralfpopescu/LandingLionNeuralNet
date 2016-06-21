"""interaction event count
engagement duration
engagemnent event count
action event count
window event count
total duration
rage clicks
scroll distance
mouse distance
scroll direction changes
mouse speed
average distance between clicks
average time between clicks"""
from NeuralNetUtil import buildExamplesFromLandingLionData, organizeListByEventType, organizeListBySession



def getInteractionEventCount(sessionData):
    interactionEventCount = 0
    return interactionEventCount

def getEngagementDuration(sessionData):
    engagementDuration = 0
    return engagementDuration

def getEngagementEventCount(sessionData):
    engagementEventCount = 0
    return engagementEventCount

def getActionEventCount(sessionData):
    actionEventCount = 0
    return actionEventCount

def getWindowEventCount(sessionData):
    windowEventCount = 0
    return windowEventCount

def getTotalDuration(sessionData):
    totalDuration = 0
    firstEvent = sessionData[0]
    lastEvent = sessionData[-1]
    return totalDuration

def getRageClicks(sessionData):
    rageClicks = False
    data = organizeListByEventType(sessionData)
    #click is event type 3
    return rageClicks

def getScrollDistance(sessionData):
    scrollDistance = 0.0
    return scrollDistance

def getMouseDistance(sessionData):
    mouseDistance = 0
    return mouseDistance

def getScrollDirectionChanges(sessionData):
    scrollDirectionChanges = 0
    return scrollDirectionChanges

def getMouseSpeed(sessionData):
    mouseSpeed = 0
    return mouseSpeed

def getAverageClickDistance(sessionData):
    averageClickDistance = 0
    return averageClickDistance

def getAverageTimeBetweenClicks(sessionData):
    averageTimeBetweenClicks = 0
    return averageTimeBetweenClicks

def isConversion(eventID):
    if eventID == 18 or eventID == 19:
        return True
    else:
        return False

def buildInVectorForSession(sessionData):
    a = getInteractionEventCount(sessionData)
    b = getEngagementDuration(sessionData)
    c = getEngagementEventCount(sessionData)
    d = getActionEventCount(sessionData)
    e = getWindowEventCount(sessionData)
    f = getTotalDuration(sessionData)
    g = getRageClicks(sessionData)
    h = getScrollDistance(sessionData)
    j = getMouseDistance(sessionData)
    h = getScrollDirectionChanges(sessionData)
    i = getMouseSpeed(sessionData)
    j = getAverageClickDistance(sessionData)
    k = getAverageTimeBetweenClicks(sessionData)
    return [a, b, c, d, e, f, g, h, i, j, k]
