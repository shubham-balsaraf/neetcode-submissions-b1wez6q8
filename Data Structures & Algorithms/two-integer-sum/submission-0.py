class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        dummy = []
        for i , n in enumerate(nums):
            if n in dummy:
                output.append(i)
                return output
            dif = target - n
            if dif in nums[i+1:]:
                dummy.append(dif)
                output.append(i)
        return None
            
