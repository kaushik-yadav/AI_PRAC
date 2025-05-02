def find(parent, node):
    # if parent and node is same that means we reached the root node
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]



def union(parent, rank, u, v):
    # finds the root node of each node
    u_root = find(parent, u)
    v_root = find(parent, v)

    # attach the lesser ranked one to the higher ranked one
    # bigger hieght tree attaches the smaller hieght tree to it

    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    elif rank[u_root] > rank[v_root]:
        parent[v_root] = u_root
    else:
        # increase the rank of node only when parent rank (u) == parent rank(v)
        parent[v_root] = u_root
        rank[u_root] += 1
    

def kruskal(nodes, edges):
    # sorting based on weight
    edges.sort(key=lambda x:x[2])
    parent = [i for i in range(nodes)]
    rank = [0] * nodes
    cost = 0
    mst = []
    for u, v, weight in edges:
        # if they have same parent that means they are connected but we dont want connected
        if find(parent, u) != find(parent, v):
            mst.append((u,v,weight))
            union(parent, rank, u, v)

            cost += weight
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print("Total Minimum Cost:", cost)
    print(rank)
    return cost

nodes = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7)
]

kruskal(nodes, edges)