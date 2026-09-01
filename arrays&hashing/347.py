class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        freq = [[] for i in range(len(nums)+1)] # { times : number }

        #saving each freq
        for n in nums:
            h[n] = 1 + h.get(n, 0)

        #adding each freq to bucked sort
        for n, times in h.items():
            freq[times].append(n)
        
        #construction of res
        res = []
        for i in range(len(freq )-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res