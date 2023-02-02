# https://leetcode.com/problems/verifying-an-alien-dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapAlphabet = {}
        inverseMapAlphabet = {}
        for i in range(26):
            mapAlphabet[order[i]] = chr(97 + i)
        
        wordsMap = []
        for i, word in enumerate(words):
            wordsMap.append('')
            for c in word:
                wordsMap[-1] += mapAlphabet[c]
        wordsMapCp = wordsMap.copy()
        wordsMap.sort()

        for i in range(len(words)):
            if wordsMapCp[i] != wordsMap[i]:
                return False
        return True
