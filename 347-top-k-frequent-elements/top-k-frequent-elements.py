from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=defaultdict(int)
        for i in nums:
            h[i]=h[i]+1
        sorts=dict(sorted(h.items(),key=lambda x:x[1],reverse=True))
        
        return list(sorts.keys())[0:k]
