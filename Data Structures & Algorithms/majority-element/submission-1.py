class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res, max_count = 0, 0
        for n in nums:
            count[n] += 1
            res = n if count[n] > max_count else res
            max_count = max(count[n], max_count)
        
        return res