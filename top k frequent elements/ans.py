class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        fres = []
        for i in nums:
            if i not in res:
                res[i]  = 1
            else:
                res[i] += 1
        sorted_items = sorted(res.items(), key=lambda x: x[1], reverse=True) # lambda x: x[1] res.items() = (1,2),(3,1) etcc... , therefore key is frequency count and the tuple is sorted
        for j in range(k):
            fres.append(sorted_items[j][0])
        return fres