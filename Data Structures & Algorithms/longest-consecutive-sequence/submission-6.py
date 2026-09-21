class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        lookup = set(nums) # O(1)

        if len(nums) <= 1:
            return len(nums)

        for x in nums: # O(n)
            if x-1 not in lookup:
                length = 1
                while x+length in lookup:
                    length += 1
                if length > longest:
                    longest = length
        return longest
                

        