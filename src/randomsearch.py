import random, time, math

def randomSearch(coordinates, timeout = 10):
    start = time.time()
    bestRoute = None
    bestDistance = math.inf

    def routeDistance(route):
        distance = 0
        for i in range(len(route) - 1):
            x1, y1 = coordinates[route[i] - 1)]
            x2, y2 = coordinates[route[i + 1] - 1)]
            distance += math.hypot(x1 - x2, y1 - y2) 
        return distance

    while time.time() - start < timeout:
        route = [1] + random.sample(range(2, len(coordinates) + 1), len(coordinates) - 1) + [1]
        d = routeDistance(route)
        if d < bestDistance:
            bestDistance, bestRoute = d, route
return math.ceil(bestDistance), bestRoute