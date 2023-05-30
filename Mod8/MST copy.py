"""

Constructs a minimum spanning tree (MST) using Prim's algorithm.

@PARAM -  G (list[list[int]]): The graph represented as an adjacency matrix.

@RETURN - list[tuple[int, int, int]]: 
            The minimum spanning tree represented as a list of tuples,
            where each tuple represents an edge in the MST as (v1, v2, weight).
"""


import heapq

def Prims(G):

    n = len(G) # Number of vertices
    #It determines the size of the graph & is used to iterate over the vertices & perform operations accordingly.

    visited = set() # Set of visited vertices
    #used to keep track of the vertices that have been visited during the construction of the (MST). 
    # It allows us to efficiently check if a vertex has already been visited or not, avoiding unnecessary computations.
   
    MST = []  #Minimum spanning tree
    #Used to store the edges that belong to the minimum spanning tree. 
    # Each edge is represented as a tuple (v1, v2, weight) 
    #   where v1 and v2 are the vertices connected by the edge 
    #   & weight is the weight/cost of the edge. 
    # The MST list gradually grows as the algorithm proceeds, adding edges that are part of the MST.

    # Create a priority queue to store edges (weight, v1, v2)
    pq = []

    # Start with vertex 0 as the initial vertex
    start_vertex = 0
    visited.add(start_vertex)

    # Add edges connected to the start vertex to the priority queue
    for v2 in range(n):
        if G[start_vertex][v2] != 0:
            heapq.heappush(pq, (G[start_vertex][v2], start_vertex, v2))

    # Continue until all vertices are visited
    while len(visited) < n:
        # Find the minimum weight edge from the priority queue
        weight, v1, v2 = heapq.heappop(pq)

        # Check if the edge connects to an unvisited vertex
        if v2 not in visited:
            # Add the edge to the minimum spanning tree
            MST.append((v1, v2, weight))
            visited.add(v2)

            # Add edges connected to the new vertex to the priority queue
            for v3 in range(n):
                if G[v2][v3] != 0 and v3 not in visited:
                    heapq.heappush(pq, (G[v2][v3], v2, v3))

    return MST
