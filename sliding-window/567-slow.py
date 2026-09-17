class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1times = [0] * 26
        for c in s1:
            s1times[ord(c) - ord("a")] += 1

        l, r = 0, len(s1)-1
        count = [0] * 26

        while r < len(s2):
            if l == 0:
                c = l
                while c <= r:
                    count[ord(s2[c]) - ord("a")] += 1
                    c+=1
            else:
                count[ord(s2[r]) - ord("a")] += 1

            if count == s1times:
                return True

            count[ord(s2[l]) - ord("a")] -= 1

            l+=1
            r+=1
        
        return False