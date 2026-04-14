class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i, n in enumerate(nums):
            if len(output) != 0 and target-n== nums[output[0]]:
                output.append(i)
                return output
            if i!=len(nums)-1 and target-n in nums[i+1:]:
                output.append(i)
        return output
        