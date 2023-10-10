import heapq
from ugraph import UndirectedGraph

euclidean_distances = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsowa": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}

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

def heuristic(node):
    return euclidean_distances[node]

def a_star_search(graph, start, goal):
    to_search = [(0, start)]
    processed = {}
    g_cost = {start: 0}

    while to_search:
        _, current_node = heapq.heappop(to_search)

        if current_node == goal:
            path = [current_node]
            while current_node != start:
                current_node = processed[current_node]
                path.append(current_node)
            path.reverse()
            return path

        for neighbor_node in graph[current_node]:
            cost_to_neighbor = g_cost[current_node] + graph[current_node][neighbor_node]

            if neighbor_node not in g_cost or cost_to_neighbor < g_cost[neighbor_node]:
                g_cost[neighbor_node] = cost_to_neighbor
                priority = cost_to_neighbor + heuristic(neighbor_node)
                heapq.heappush(to_search, (priority, neighbor_node))
                processed[neighbor_node] = current_node

    return None

def greedy_search(graph, start, goal, heuristic):
    path = [start]
    
    while path[-1] != goal:
        current_node = path[-1]
        neighbors = graph[current_node]
        
        if not neighbors:
            return None
        
        next_node = min(neighbors, key=lambda neighbor: heuristic(neighbor))
        
        path.append(next_node)
    
    return path

start_node = "Arad"
goal_node = "Bucharest"

path = a_star_search(romania_map.graph_dict, start_node, goal_node)

if path:
    print("A star Path:", path, romania_map.path_weight(path))
else:
    print("No path found.")

path = greedy_search(romania_map.graph_dict, start_node, goal_node, heuristic)

if path:
    print("Greedy Path:", path, romania_map.path_weight(path))
else:
    print("No path found.")
