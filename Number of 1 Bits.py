class Solution:
    def hammingWeight(self, n: int) -> int:
        l=bin(n)
        k=str(l)
        count=0
        for i in range(len(k)):
          if k[i]=='1':
            count+=1 
        return count       
