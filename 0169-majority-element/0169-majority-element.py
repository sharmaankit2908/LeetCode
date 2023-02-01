class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=1
        maj=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==maj:
                cnt +=1
            elif cnt==0:
                maj=nums[i]
                cnt +=1
            else:
                cnt -=1
        return maj
                
        # count=0
        # for i in range(len(nums)):
        #     if nums[i]==maj:
        #         count +=1
        # if count >= int(len(nums)/2):
            
        