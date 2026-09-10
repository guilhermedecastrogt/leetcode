class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        l, r = 0, 1
        h = set()
        h.add(s[0])
        m = 1

        while r <= (len(s)-1):
            while s[r] in h:
                h.remove(s[l])
                l += 1
                
            h.add(s[r])
            m = max(m, (r - l) + 1)
            r += 1
        
        return m