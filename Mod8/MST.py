import heapq

def Prims(G):
    n = len(G)
    visited = set()
    MST = []

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
