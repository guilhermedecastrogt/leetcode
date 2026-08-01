class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        p = 0;
    
        while p < len(nums):
            x = target - nums[p]
            if x in map:
                r.append(map[x])
                r.append(nums[p])
                return r;
            map[nums[p]] = p;
            p += 1
                