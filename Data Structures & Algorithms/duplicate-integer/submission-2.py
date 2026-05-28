class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sets store only 1 of the number

        return len(set(nums)) < len(nums)