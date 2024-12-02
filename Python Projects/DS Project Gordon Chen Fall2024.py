# Data Visualization Attempt


# import random
# import networkx as networkx
# import matplotlib.pyplot as plot

# def generate_graph(maxNodes, density = 0.5):
#     graph = networkx.Graph()
#     graph.add_nodes_from(range(maxNodes))
#     for i in range(maxNodes):
#         for j in range(i+1, maxNodes):
#             if random.random() < density:
#                 distance = random.randint(1,10)
#                 graph.add_edge(weight = distance)
#     return graph

# graph = generate_graph(10)

#Functionality

import random

class node:
    def __init__(self, x, y, z, identity):
        self.coordinates = [x,y,z]
        self.nextNodes = []
        self.identifier = identity

def distanceWeight(initial, next): #Extra noted challenge: Dijkstra's algorithm doens't work with negative weights, so absolute value/magnitudes are necessary in this distance weight calculation
    diff = []
    for i in range(len(initial.coordinates)):
        diff.append(next.coordinates[i]-initial.coordinates[i])
    distanceWeight = 0   
    for i in diff:
        distanceWeight = distanceWeight + i**2
    distanceWeight = distanceWeight**0.5
    return distanceWeight

def graphArrayGeneration(maxNodes):
    letters = ["A","B","C","D","E","F","G","H","I","J","K"] #Max of 11 for demonstration purposes
    array = []
    for i in range(maxNodes):
        newNode=node(random.randrange(0,10), random.randrange(0,10), random.randrange(0,10), letters[i])
        array.append(newNode)
    for i in range(random.randrange(maxNodes*10)): #Density of Edges
        num1 = random.randrange(maxNodes)
        num2 = random.randrange(maxNodes)
        while num1 == num2:
            num2 = random.randrange(maxNodes)
        weight = distanceWeight(array[num1], array[num2])
        array[num1].nextNodes.append([array[num2].identifier, weight])
        array[num2].nextNodes.append([array[num1].identifier, weight])        
    return array

def findNodeIndex(graph, given):
    indexCount = 0
    for i in graph:
        if i.identifier == given:
            return indexCount
        else:
            indexCount+=1

def dijkstra(graph, startIndex, targetIndex):
    path = [] 
    infinity = 999 #Substitue for Infinity
    active = True
    distancesfromStart = []
    for i in range(len(graph)):
        distancesfromStart.append(infinity) 
    distancesfromStart[startIndex] = 0
    unvisitedDistancesfromStart = distancesfromStart
    while active:
        print("Loop Pass")
        currNodeIndex = unvisitedDistancesfromStart.index(min(unvisitedDistancesfromStart))
        print(currNodeIndex)
        if len(unvisitedDistancesfromStart) == 0 or min(unvisitedDistancesfromStart) == infinity or graph[currNodeIndex] == graph[targetIndex]: # Modify the distancefromStart array at some point
            break
        else:
            for i in range(len(graph[currNodeIndex].nextNodes)):
                nextNodeIndex = findNodeIndex(graph, graph[currNodeIndex].nextNodes[i][0])
                testDistance = graph[currNodeIndex].nextNodes[i][1] + distancesfromStart[currNodeIndex]
                print("Next Node Index: " + str(nextNodeIndex))
                print("testDistance: " + str(testDistance))
                print("Length of distancesfromStart: " + str(len(distancesfromStart)))
                if testDistance < distancesfromStart[nextNodeIndex]: 
                    distancesfromStart[nextNodeIndex] = testDistance
                    # for i in reversed(path):
                    #     if i == graph[findNodeIndex(graph, i)].identifier:
                    #         break
                    #     path.pop(findNodeIndex(reversed(path), i))
                    # path.append(graph[nextNodeIndex].identifier)
                else:
                    continue
            unvisitedDistancesfromStart[currNodeIndex] = infinity
    total = [distancesfromStart, path]
    return total


           


    #if == 999 -> No path found



graph = graphArrayGeneration(10)
for i in graph:
    print(i.identifier)
    print(i.coordinates)
    print(i.nextNodes)
print("Graph Generated")
startIndex = 0
targetIndex = 9
total = dijkstra(graph, startIndex, targetIndex)
print("Shortest distance from starting node to each respective ending node: " + str(total[0]))
print("Shortest distance from starting node to target node: " + str(total[0][targetIndex]))
print("(Not fully implemented) Shortest Path (Nodes to Visit) from Start Node to Ending Node: " + str(total[1]))
print("Dijkstra Completed")



