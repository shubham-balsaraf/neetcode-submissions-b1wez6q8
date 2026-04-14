class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)-1):
            if nums[x] in nums[:x] or nums[x] in nums[x+1:]:
                return True
        return False