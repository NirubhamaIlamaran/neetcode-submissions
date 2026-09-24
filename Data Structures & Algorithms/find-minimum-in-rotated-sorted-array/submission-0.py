class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)/2
            if left<right:
                return nums[left]
            if mid>r:
                l=mid+1
            if mid<r:
                return mid
        


        
        