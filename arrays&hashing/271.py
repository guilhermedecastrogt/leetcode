class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for w in strs:
            res += str(len(w)) + "#" + w
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        p = 0;

        while p < len(s):
            i = p
            while s[i] != "#":
                i += 1
            length = int(s[p:i])
            res.append(s[i + 1 : i + 1 + length])
            p = i + 1 + length

        return res