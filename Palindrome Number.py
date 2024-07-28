class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        s=0
        while(x>0):
            d=x%10
            s=s*10+d
            x=x//10
        return s==temp

    
        
