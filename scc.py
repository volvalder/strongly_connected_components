class Graph:
    def __init__(self, pairs):
        self.adjList = {}
        self.revList = {}

        for pair in pairs:
            self.addNode(self.adjList, pair[0])
            self.addNode(self.adjList, pair[1])
            self.addNode(self.revList, pair[0])
            self.addNode(self.revList, pair[1])
            
            self.addEdge(self.revList, pair[1], pair[0])
            self.addEdge(self.adjList, pair[0], pair[1])

        self.ids = [None] * len(self.revList)
        self.count = 0
        self.stack = []
        
    def addNode(self, target, n):
        if n not in target:
            target[n] = []

    def addEdge(self, target, n, e):
        target[n].append(e)

    # running this as in topological sort
    # to retrieve same order of vertices
    def preorderDfs(self, v, visited = set()):
        visited.add(v)
        for neighbor in self.revList[v]:
            if neighbor not in visited:
                self.preorderDfs(neighbor, visited)
                self.stack.append(neighbor)
    # same dsf with adding vertice to a component 
    def dfs(self, v, visited):
        visited.append(v)
        self.ids[v] = self.count
        for neighbor in self.adjList[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def scc(self):
        # first we run preorder dfs and store that order in a stack
        for vert in self.revList.keys():
            self.preorderDfs(vert)
        # then we are dfsing again, now through vertices taken from a stack
        visited = []
        while(self.stack):
            v = self.stack.pop()
            if v not in visited:
                self.dfs(v, visited)
                # every time we find a component that is not in visited
                # means that it is not connected to a previous group
                self.count+=1