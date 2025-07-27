class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dict = {} 
        result = []
        for s in strs:
            sorted_s  = tuple(sorted(s))
            if sorted_s not in anagram_dict:
                anagram_dict[sorted_s] = []
            anagram_dict[sorted_s].append(s)
        for value in anagram_dict.values():
            result.append(value)
        return result