def average(array):
    plantsSet = set(array)
    distinctHeights = len(plantsSet)
    distinctHeightsSum = sum(plantsSet)
    return distinctHeightsSum/distinctHeights

