class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        sety = {nums[0]}

        for x in nums[1:]:
            if x in sety:
                return True
            sety.add(x)
        return False

        