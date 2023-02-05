# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        def isAnagram(map1, map2):
            for k in map1:
                if map1[k] != map2.get(k, 0):
                    return False
            return True
        
        if len(p) > len(s):
            return result
        n, m = len(s), len(p)
        map1, map2 = {}, {}
        for i in range(m):
            map1[p[i]] = map1.get(p[i], 0) + 1
            map2[s[i]] = map2.get(s[i], 0) + 1
        
        for i in range(n - m + 1):
            if isAnagram(map1, map2):
                result.append(i)
            if i+m == n:
                break
            map2[s[i]] -= 1
            map2[s[i+m]] = map2.get(s[i+m], 0) + 1

        return result
        
