from ugraph import UndirectedGraph

romania_map = UndirectedGraph({
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99},
    'Hirsova': {'Urziceni': 98},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97},
    'Rimnicu': {'Sibiu': 80},
    'Urziceni': {'Vaslui': 142},
})

start_node = 'Arad'
goal_node = 'Bucharest'

dfs_path = romania_map.dfs(start_node, goal_node)
bfs_path = romania_map.bfs(start_node, goal_node)
ucs_path = romania_map.ucs(start_node, goal_node)

dfs_weight = romania_map.path_weight(dfs_path)
bfs_weight = romania_map.path_weight(bfs_path)
ucs_weight = romania_map.path_weight(ucs_path)

print("DFS Path:", dfs_path)
print("DFS Weight:", dfs_weight)

print("BFS Path:", bfs_path)
print("BFS Weight:", bfs_weight)

print("UCS Path:", ucs_path)
print("UCS Weight:", ucs_weight)