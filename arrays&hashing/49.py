class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        pM = 0

        while pM < len(strs):
            arr = strs[pM]
            freq = {}

            p = 0
            while p < len(arr):
                if arr[p] in freq:
                    freq[arr[p]] += 1
                else:
                    freq[arr[p]] = 1
                p += 1

            key = tuple(sorted(freq.items()))

            if key not in hash:
                hash[key] = []
            hash[key].append(arr)
            pM += 1

        return list(hash.values())


    # O(n . m log m) using sorted