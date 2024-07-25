class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num=[1]
        i2=0
        i3=0
        i5=0
        while len(num)<n:
            next2=num[i2]*2
            next3=num[i3]*3
            next5=num[i5]*5
            next=min(next2,next3,next5)
            if next == next2:
                i2+=1
            if next == next3:
                i3+=1
            if next == next5:
                i5+=1
            num.append(next)
        return num[-1]
