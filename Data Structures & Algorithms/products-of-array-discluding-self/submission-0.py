class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a,b,c,d]
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]
        # [48,1*24,2*6,8]

        before = [1 for x in range(len(nums))]
        after = [1 for x in range(len(nums))]
        prev = 1
        for x in range(len(nums)):
            before[x] = prev
            prev = nums[x]*prev

        d = 1
        for y in range(len(nums)-1,-1, -1): # )
            after[y] = d
            d = nums[y]*d

        for x in range(1,len(after)):
            after[x]=before[x]*after[x]
    
        return after


            