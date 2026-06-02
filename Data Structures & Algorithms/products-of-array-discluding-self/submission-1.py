class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1 for x in range(len(nums))]
        prev = 1
        for x in range(len(nums)):
            before[x] = prev
            prev = nums[x]*prev

        d = 1
        for y in range(len(nums)-1,-1, -1): # )
            before[y] *= d
            d = nums[y]*d
        return before


            