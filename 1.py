class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} # {value, position}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in h:
                return [h[diff], i]
            h[n] = i
        
        return []

#On time On space