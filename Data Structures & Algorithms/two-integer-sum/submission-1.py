class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1,p2 = 0,0
        for i, n in enumerate(nums):
            if target-n in nums[i+1:]:
                p1 = i
                p2 = nums.index(target-n, i+1)
                break
        return [p1,p2]
    