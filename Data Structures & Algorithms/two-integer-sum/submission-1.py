class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # edge: len nums is 2 and if first 2 are our ans
        if nums[0] + nums[1] == target:
            return [0,1]
        
        count = {}
        for x in range(len(nums)):
            a = target - nums[x]
            if a in count.keys():
                return [count[a], x]
            count[nums[x]] = x

# x=0, a=10-4=6, count : {"6:0"}
# x=1, a=10-5=5, count : {"6:0", "5:1"}
# x=2, a=10-6=4
