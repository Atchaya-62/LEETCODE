class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev=nums[nums[0]]
        curr=nums[nums[nums[0]]]

        while prev!= curr:
            prev=nums[prev]
            curr=nums[nums[curr]]

        prev=nums[0]
        while prev!=curr:
            prev=nums[prev]
            curr=nums[curr]
        return prev
