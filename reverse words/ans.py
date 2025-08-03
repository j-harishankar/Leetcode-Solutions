class Solution(object):
    def reverseWords(self, s):
        k =  s.strip()
        l = k.split()  
        a = " ".join(l[::-1])
        return a
