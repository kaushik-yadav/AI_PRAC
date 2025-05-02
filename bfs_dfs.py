from collections import deque

def dfs(graph, node, visited):
    # marking the first node as visited
    visited.add(node)
    nodes.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


        
nodes = []
visited = set()
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}


def bfs(graph, queue, visited):
    if not queue:
        return
    node = queue.popleft()
    if node not in visited:
        nodes.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    bfs(graph, queue, visited)


start_node = 0
queue = deque()
queue.append(start_node)
# start from node 0
#dfs(graph, start_node, visited)
#print(f'DFS Sequence : {nodes}')
bfs(graph, queue, visited)
print(f'BFS Sequence : {nodes}')

