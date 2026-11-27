class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = defaultdict(int)

        for num in nums:

            top[num] += 1 
        
        cutoff = sorted(top.values(), reverse=True)[:k]

        keys = [k for k, v in top.items() if v in cutoff]
        
        return keys