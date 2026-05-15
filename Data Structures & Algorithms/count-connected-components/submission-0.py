class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            for nbr in graph[node]:
                if nbr not in visited:
                    print(nbr)
                    visited.add(nbr)
                    dfs(nbr)
    
        components = 0
        for node in graph:
            if node not in visited:
                components += 1
                visited.add(node)
                dfs(node)

        return components