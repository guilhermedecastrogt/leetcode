class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        p = 0
        pos = 1

        #prefix ->
        while p < len(nums):
            if p != 0:
                res[p] = nums[p-1] * pos
                pos = res[p]
            else:
                res[p] = 1
            print(res)
            p+=1

        pos = 1
        p -= 1

        #sufix <-
        while p >= 0:
            res[p] *= pos;
            pos *= nums[p]
            p-=1

        return res

#O(n+n) == O(n) time
#O(1) aditional space