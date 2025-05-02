import heapq

# mst def: mst should have n nodes and (n-1) edges i.e no connected comp

def prims(adj_list, start):
    visited = set()
    # adding weight, vertex and the parent node
    # for start node we have no parent
    min_heap = [(0, start, -1)]
    cost = 0
    mst_seq = []
    while min_heap:
        weight, node, parent  = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            cost += weight

            if parent != -1:
                # if it is not the first node
                # add the sequence in list
                mst_seq.append([parent, node, weight])
            
            for neighbour, wt in adj_list[node]:
                # traversing the adj_list 
                if neighbour not in visited:
                    heapq.heappush(min_heap, (wt, neighbour, node))

    print("Edges in MST:")
    for u, v, w in mst_seq:
        print(f"{u} - {v} with weight {w}")
    print("Total Minimum Cost:", cost)

    return mst_seq

adj_list = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}
start_node = 0
mst_seq = prims(adj_list, start_node)
print(*mst_seq)