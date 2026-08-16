class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        temp = 0
        l, r = 0, 1
        stack = []
        wtemp_season = 0

        while r < len(height):
            if height[l] > height[r]:
                wtemp = 0
                start = r

                while stack and stack[-1][1] < height[r]:
                    v = stack.pop()
                    width = start - v[0]
                    wtemp += (height[r] - v[1]) * width
                    start = v[0]

                wtemp_season += wtemp
                res += wtemp
                stack.append([start, height[r]])
                temp += height[r]
                r += 1

            elif height[l] <= height[r]:
                res += ((height[l] * ((r - 1) - l)) - temp) - wtemp_season
                wtemp_season = 0
                temp = 0
                stack = []
                l = r
                r += 1

        return res


    