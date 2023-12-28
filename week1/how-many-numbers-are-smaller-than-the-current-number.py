

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        prefix_sum = {}
        total = 0
        for key in sorted(count.keys()):
            prefix_sum[key] = total
            total += count[key]

        res = [prefix_sum[num] for num in nums]
        return res
