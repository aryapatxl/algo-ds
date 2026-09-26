class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,5,7,8] target = 7
        y = len(numbers)-1
        x = 0
        while x < y:
            cur = numbers[x] + numbers[y]
            if cur > target:
                y -= 1
            
            elif cur < target:
                x += 1
        
            else:
                return [x+1,y+1]




