class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}

        for i in range(n):
            graph[i] = []

        queue = [source]
        visited = {source}

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        while queue:
            vertex = queue.pop(0)

            if vertex == destination:
                return True
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False    

        
