class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum=1
        output=[0]*len(nums)
        zero_count=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                zero_count+=1
            else:
                sum*=nums[i]
        if zero_count>1:
            return output
        if zero_count==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    output[i]=sum
                else:
                    output[i]=0
            return output

        for i in range(0,len(nums)):
            output[i]=sum//nums[i]
        return output
        

        