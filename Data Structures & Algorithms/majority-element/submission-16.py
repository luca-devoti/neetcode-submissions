class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        items = {}
        checker = len(nums) / 2

        for num in nums:
            if num in items:
                items[num] += 1
            else:
                items[num] = 1

            if items[num] > checker:
                return num
            
