#optimal solution //O(m*n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            key = [0] * 26
            for c in i:
                key[ord(c) - ord("a")] += 1 
            res[tuple(key)].append(i)
        return list(res.values())