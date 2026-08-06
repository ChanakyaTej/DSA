class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        x=n
        while x>=n: 
            p=1
            x2=x
            while x2!=0:
                p=p*(x2%10)
                x2=x2//10
            if p%t==0:
                return x
            else:
                x=x+1