class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # O(n), n=len(nums)
        prev = -1
        for x in nums: # O(n)
            if x == prev:
                return True
            prev=x
        return False

# O(n) + O(n) = O(n)