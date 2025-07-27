class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set() # here initalize a set to reduce time complexity if i used list here searching alone would take O(n) complexity
        max_len = min(len(s),1)
        start = 0 
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start]) # remove all the elements until the repeating letter comes  abcabc -> abc
                start += 1
            seen.add(s[i])
            length = i - start + 1
            max_len = max(max_len,length)        
        return max_len