class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            if count[n] > len(nums)//2:
                return n
            
            count[n] += 1
        
        for n in nums:
            if count[n] > len(nums)//2:
                return n