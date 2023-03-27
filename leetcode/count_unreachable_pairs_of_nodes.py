# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        #union find
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

        for n1, n2 in edges:
            union(n1, n2)

        p1 = set(par)
        m = len(p1)
        while True:
            for n1, n2 in edges:
                union(n1, n2)
            p1 = set(par)
            if m == len(p1):
                break
            m = len(p1)
        
        clusters = defaultdict(lambda: 0)
        for p in par:
            clusters[p] += 1
        

        result = 0
        for p in clusters:
            result += clusters[p] * (n - clusters[p])
        return result // 2
        
