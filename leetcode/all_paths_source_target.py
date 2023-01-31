# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = [0]
        visited = set()
        n = len(graph)
        def dfs(idx):
            if len(path) > 0 and path[-1] == n - 1:
                result.append(path.copy())
                return
            for i in graph[idx]:
                if i in visited:
                    continue
                visited.add(i)
                path.append(i)
                dfs(i)
                path.pop()
                visited.remove(i)
        
        dfs(0)
        return result
