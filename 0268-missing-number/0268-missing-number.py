class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Method 1
        # nums.sort()
        # for i in range(len(nums)):
        #     if i !=nums[i]:
        #         return i
        # return len(nums)

        # Method 2
        # maxi=max(nums)
        # dummy=[0]*(maxi+2)
        # for i in range(len(nums)):
        #     dummy[nums[i]]=dummy[nums[i]]+1
        # for i in range(len(dummy)):
        #     if dummy[i]==0:
        #         return i

        # Method 3
        # sum1=sum(nums)
        # l=len(nums)+1
        # sum2=l*(l-1)*0.5
        # return int(sum2-sum1)

        # Method 4
        a1,a2=0,0
        mini=min(nums)
        if mini !=0:
            return 0
        a1,a2=0,0
        for i in range(len(nums)+1):
            a1 ^=i
        for i in range(len(nums)):
            a2 ^=nums[i]
        return a1^a2