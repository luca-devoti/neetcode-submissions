class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, v in enumerate(nums):
            value_needed = target - v
            if value_needed in table:
                return [table[value_needed], i]
            table[v] = i
            
