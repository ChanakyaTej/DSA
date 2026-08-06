class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        arr=[]
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]]=[i]
            elif groupSizes[i]  in d:
                d[groupSizes[i]].append(i)
            if len(d[groupSizes[i]])==groupSizes[i]:
                arr.append(d[groupSizes[i]])
                d[groupSizes[i]]=[]
        return arr