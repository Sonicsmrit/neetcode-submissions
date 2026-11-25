class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pure = {}

        for idx,i in enumerate(nums):
            sub = target - i

            if i in pure:
                return [pure[i], idx]

            pure[sub] = idx

        return []
        