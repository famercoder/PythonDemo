from cmath import inf
#狄克斯特拉算法(带权最短路径问题)
graph = {
    "home":{"v1":4, "v2":3, "v3":10},
    "v1":{"v3":3, "v4":8},
    "v2":{"v3":5, "v6":12},
    "v3":{"v4":3, "v5":12},
    "v4":{"v5": 3, "school":5},
    "v5":{"school":1},
    "v6":{"school":2},
    "school":{},
}

def initRow(costs, key, cost):
    costs[key] = {}
    costs[key]["father"] = None
    costs[key]["checked"] = False
    costs[key]["cost"] = cost

def findLowerCostNode(costs):
    key = None
    cost = float(inf)

    for name in costs:
        item = costs[name]
        if item["checked"] == False and item["cost"] < cost:
            cost = item["cost"]
            key = name
 
    return key

def dijkstra(graph, start, end):
    costs = {}
    initRow(costs, start, 0)
    key = findLowerCostNode(costs)

    while key != None and key != end:
        neighbors = graph[key].keys()
        for neighbor in neighbors:
            if neighbor not in costs:
                initRow(costs, neighbor, float(inf))

            newCost = graph[key][neighbor] + costs[key]["cost"]
            if newCost < costs[neighbor]["cost"]:
                costs[neighbor]["cost"] = newCost
                costs[neighbor]["father"] = key

        costs[key]["checked"] = True
        key = findLowerCostNode(costs)

    key = end
    routers = []

    while key != None:
        routers.insert(0, key)
        key = costs[key]["father"]
    
    print(f'router:{"->".join(routers)}, cost:{costs[end]["cost"]}')

dijkstra(graph, "home", "school")

