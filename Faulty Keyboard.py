class Solution:
    def finalString(self, s: str) -> str:
        t=[]
        for l in s:
            if l=='i':
                t=t[::-1]
            else:
                t.append(l)
        return "".join(t)
        
