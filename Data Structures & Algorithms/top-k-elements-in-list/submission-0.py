from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for _ in range(len(nums)+1)]

        freq = Counter(nums)

        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(nums),0,-1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result

        