class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while(n!=1):
            sq=0
            while n>0:
             d=n%10
             sq+=d**2
             n=n//10
            if sq in a:
              return False
            a.add(sq)
            n=sq
        return True


        
        
