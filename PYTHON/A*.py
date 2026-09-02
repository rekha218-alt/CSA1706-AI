graph = {
'A':[('B',1),('C',3)],
'B':[('D',3),('E',6)],
'C':[('F',5)],
'D':[],
'E':[('G',2)],
'F':[('G',2)],
'G':[]
}

heuristic = {
'A':7,
'B':6,
'C':4,
'D':3,
'E':2,
'F':1,
'G':0
}

open_list = [('A',0)]

visited = []

while open_list:

    open_list.sort(key=lambda x:x[1]+heuristic[x[0]])

    node,cost = open_list.pop(0)

    if node in visited:
        continue

    print(node,end=" ")

    visited.append(node)

    if node=='G':
        print("\nGoal Reached")
        break

    for neighbour,value in graph[node]:

        if neighbour not in visited:

            open_list.append((neighbour,cost+value))
