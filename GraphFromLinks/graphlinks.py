"""
Name: graphlinks
Purpose: Create a program that will create a graph or network from a series of links
Author: Bruno Albuquerque
Date: 06/01/2022
"""

#Function to create dictionary corresponding to the graph
def fromlinks(links):
    graph = {}
    for link in links:
        for node in link:
            if not node in graph:
                graph[node] = []
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    print(graph)

#Implementation 
fromlinks([(1,2),(1,4),(2,3),(3,4)])
