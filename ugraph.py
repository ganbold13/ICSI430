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