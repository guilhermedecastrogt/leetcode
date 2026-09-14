class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                subarr = []
                target = n + nums[l] + nums[r]
                if target > 0:
                    r-=1
                elif target < 0:
                    l+=1
                else:
                    subarr.append(n)
                    subarr.append(nums[l])
                    subarr.append(nums[r])

                    res.append(subarr)
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return res