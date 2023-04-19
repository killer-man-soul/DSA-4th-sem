graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}


# Prims Algorithm

def prim_mst(graph):
    mst = set()
    visited = set()
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    while len(visited) != len(graph):
        min_edge = None
        for vertex in visited:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (vertex, neighbor, weight)
        mst.add(min_edge)
        visited.add(min_edge[1])

    return mst

mst = prim_mst(graph)
print("Minimum Spanning Tree using Prims:")
for edge in mst:
    print(edge[0], "-", edge[1], ": ", edge[2])


def kruskal_mst(graph):
    # Initialize variables
    mst = set()
    vertices = set(graph.keys())
    parent = {vertex: vertex for vertex in vertices}
    rank = {vertex: 0 for vertex in vertices}
    edges = []

    # Add all edges to the edges list and sort by weight
    for vertex in vertices:
        for neighbor, weight in graph[vertex].items():
            edges.append((vertex, neighbor, weight))
    edges.sort(key=lambda x: x[2])

    # Loop through all edges and add to MST if it does not create a cycle
    for edge in edges:
        root1 = find(parent, edge[0])
        root2 = find(parent, edge[1])
        if root1 != root2:
            mst.add(edge)
            union(parent, rank, root1, root2)

    return mst

def find(parent, vertex):
    # Find the root of the set that vertex belongs to
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(parent, rank, root1, root2):
    # Merge the two sets by rank
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root2] > rank[root1]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        rank[root1] += 1
mst_kruskal = kruskal_mst(graph)
print("Minimum Spanning Tree using Kruskals:")
for edge in mst_kruskal:
    print(edge[0], "-", edge[1], ": ", edge[2])
