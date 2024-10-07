class Solution:
    def numSquares(self, n: int) -> int:
        k=[n]*(n+1)
        k[0]=0
        k[1]=1
        for i in range(2,n+1):
            j=1
            while (j*j <=i ):
                k[i]=min(k[i],k[i-(j*j)]+1)
                j+=1
        return k[n]
        
