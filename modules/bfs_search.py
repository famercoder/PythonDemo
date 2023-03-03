from collections import deque

graph={}
graph["you"]=["alice", "bob", "claire"]
graph["bob"]=["anuj", "peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom", "jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]

def bfsSearch(name):
    dq = deque(graph[name])
    searched = []

    while len(dq) > 0:
        person = dq.popleft()
        if person[-1] == 'm' and person not in searched:
            return person 
        
        dq.extend(graph[person])
        searched.append(person)

    return "Not found!"

person = bfsSearch("you")
print(person)