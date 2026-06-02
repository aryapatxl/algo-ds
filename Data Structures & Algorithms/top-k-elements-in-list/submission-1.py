from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## bucketsort O(n) solution
        count = Counter(nums)
        arr = [[] for x in range(len(nums) +1 )] ## fixed size arr

        # append values in nums to their count indicies
        for num, c in count.items():
            arr[c].append(num)
        
        ans = []
        # loop thru the count indicies arr and append top k vals to ans
        # loop from high to low
        for j in range(len(arr)-1, 0, -1):
            for num in arr[j]:
                ans.append(num)
            if len(ans) == k:
                return ans