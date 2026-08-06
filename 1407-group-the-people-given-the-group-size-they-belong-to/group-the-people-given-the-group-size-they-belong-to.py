from collections import defaultdict
class Solution:
    def groupThePeople(self, a: List[int]) -> List[List[int]]:
        d=defaultdict(list)
        arr=[]
        for j,i in enumerate(a):
                d[i].append(j)
                if len(d[i])==i:
                    arr.append(d[i])
                    d[i]=[]
        return arr