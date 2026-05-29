class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3 -> 0
        # 4 -> 1
        # 5 -> 2
        # 6 -> 3

        if len(nums) == 2:
            return [0,1]

        hashy = {}
        for index in range(len(nums)): # O(n), O(n)
            numToFind= target - nums[index]
            if numToFind in hashy.keys():
                return [hashy[numToFind], index]
            hashy[nums[index]] = index
                