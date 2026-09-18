class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum={0:1}
        count=0
        currsum=0
        for num in nums:
            currsum+=num
            diff=currsum-k
            if diff in prefixSum:
                count+=prefixSum[diff]
            prefixSum[currsum]=prefixSum.get(currsum,0)+1
        return count


        