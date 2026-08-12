class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        temp = 0
        l, r = 0, 1

        while r < len(height)-1:
            if height[l] > height[r]:
                temp += height[r]
                r+=1
            elif height[l] <= height[r]:
                res += (height[l]*((r-1)-l))-temp
                print(temp)
                temp = 0
                l = r
                r+=1
        return res