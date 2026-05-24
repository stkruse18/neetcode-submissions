from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cow = defaultdict(int)

        for num in nums:
            cow[num] += 1

        sorted_keys = sorted(cow, key=cow.get, reverse=True)

        return sorted_keys[:k]
        



            
        