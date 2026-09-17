class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6]
        #[1,1,2,8]
        pre=[1 for x in range(len(nums))]
        #[1,1,1,1]
        num = 1
        for x in range(len(nums)):
            pre[x] = num
            num *= nums[x]
  

        #suffix
        #[1,2,4,6]
        temp = 1
        for x in range(len(nums)-1,-1,-1):
            pre[x]*=temp
            temp*=nums[x]
        return pre

        
        



