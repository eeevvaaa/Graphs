"""
Simple graph implementation
"""
class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: return None

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else: return None

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            return None

    def add_edge(self, vertex_one, vertex_two):
        if vertex_one in self.vertices and vertex_two in self.vertices:
            self.vertices[vertex_one].add(vertex_two)
            self.vertices[vertex_two].add(vertex_one)

    def bft(self, starting_vertex):
        queue = Queue()
        visited = []

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            current_node = queue.dequeue()
            visited.append(current_node)
            for edge in self.vertices[current_node]:
                if edge not in visited:
                    queue.enqueue(edge)
        return visited

    def dft(self, starting_vertex):
        stack = Stack()
        visited = []

        stack.push(starting_vertex)

        while stack.size() > 0:
            current_node = stack.pop()
            visited.append(current_node)
            for edge in self.vertices[current_node]:
                if edge not in visited:
                    stack.push(edge)
        return visited

    def dft_r(self, starting_vertex, visited = None):
        if visited == None:
            visited = []
        if starting_vertex not in visited:
            visited.append(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_r(edge, visited)
        return visited

    def bfs(self, starting_vertex, target_vertex):
        queue = Queue()
        visited = []

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            current_node = queue.dequeue()
            visited.append(current_node)
            for edge in self.vertices[current_node]:
                if edge not in visited:
                    if edge == target_vertex:
                        return True
                    queue.enqueue(edge)
        return False

    def dfs(self, starting_vertex, target_vertex):
        stack = Stack()
        visited = []

        stack.push(starting_vertex)

        while stack.size() > 0:
            current_node = stack.pop()
            visited.append(current_node)
            for edge in self.vertices[current_node]:
                if edge not in visited:
                    if edge == target_vertex:
                        return True
                    stack.push(edge)
        return False
