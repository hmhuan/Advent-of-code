# https://leetcode.com/problems/jump-game-iv/submissions/909404848/
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        values = {}
        for i in range(n):
            if arr[i] in values:
                values[arr[i]].append(i)
            else:
                values[arr[i]] = [i]
        
        visited = [False] * n
        visited[0] = True
        queue = [0]
        steps = 0
        target = n - 1
        
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr == target:
                    return steps
                
                if curr - 1 >= 0 and not visited[curr - 1]:
                    visited[curr - 1] = True
                    queue.append(curr - 1)
                
                if curr + 1 < n and not visited[curr + 1]:
                    visited[curr + 1] = True
                    queue.append(curr + 1)
                

                if arr[curr] in values:
                    for index in values[arr[curr]]:
                        if not visited[index]:
                            visited[index] = True
                            queue.append(index)
                    del values[arr[curr]]
            
            steps += 1
        
        return -1
