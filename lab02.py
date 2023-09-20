from collections import deque
import heapq

class UndirectedGraph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        else:
            self.graph_dict = {}
            for vertex in graph_dict:
                self.add_vertex(vertex)
                for neighbor, weight in graph_dict[vertex].items():
                    self.add_edge(vertex, neighbor, weight)
        

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph_dict[vertex1][vertex2] = weight
        self.graph_dict[vertex2][vertex1] = weight

    def __str__(self):
        result = ""
        for vertex, edges in self.graph_dict.items():
            result += f"{vertex} -> {', '.join([f'{k}({v})' for k, v in edges.items()])}\n"
        return result
    
    def dfs(self, start, goal):
        visited = set()
        stack = [(start, [])]

        while stack:
            current, path = stack.pop()
            if current == goal:
                return path + [current]
            if current not in visited:
                visited.add(current)
                for neighbor, _ in sorted(self.graph_dict[current].items()):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [current]))

        return None

    def bfs(self, start, goal):
        visited = set()
        queue = deque([(start, [])])

        while queue:
            current, path = queue.popleft()
            if current == goal:
                return path + [current]
            if current not in visited:
                visited.add(current)
                for neighbor in sorted(self.graph_dict[current]):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [current]))

        return None

    def ucs(self, start, goal):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            cost, current, path = heapq.heappop(priority_queue)
            if current == goal:
                return path + [current]
            if current not in visited:
                visited.add(current)
                for neighbor, weight in sorted(self.graph_dict[current].items(), key=lambda x: x[0]):
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + weight, neighbor, path + [current]))

        return None
    
    def path_weight(self, path):
        total_weight = 0
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            if next_node in self.graph_dict[current_node]:
                total_weight += self.graph_dict[current_node][next_node]
            
        return total_weight


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