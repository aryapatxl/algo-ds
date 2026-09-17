class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        hashy = {}

        # O(n), count
        for x in nums:
            if x in hashy:
                hashy[x] += 1
            else:
                hashy[x] = 1
        # O(n), sort into 'buckets'
        arr = [[] for x in range(len(nums)+1)]
        for num, count in hashy.items():
            arr[count].append([num])

        ans = []
        # decr length of the array by 1 and start at 1, start at the end
        for i in range(len(arr)-1,0,-1):
            for number in arr[i]:
                ans += number
                if len(ans) == k:
                    return ans






   