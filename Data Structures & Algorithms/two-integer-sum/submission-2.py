class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        for i,n in enumerate(nums):
            indices[n]=i
        for i in range(0,len(nums)-1):
            complement=target-nums[i]
            if complement in indices and indices[complement]!=i:
                return [i,indices[complement]]
        return []

        