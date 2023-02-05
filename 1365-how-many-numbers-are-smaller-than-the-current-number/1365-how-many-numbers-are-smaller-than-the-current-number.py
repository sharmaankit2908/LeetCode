class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # Method 1 Brute force approach O(n*n) Time coplexity
        # ans=[]
        # n=len(nums)
        # for i in range(n):
        #     c=0
        #     for j in range(n):
        #         if j !=i and nums[j]<nums[i]:
        #             c +=1
        #     ans.append(c)
        # return ans
                    
        # Method 2 
        dic={}
        for k,v in enumerate(sorted(nums)):
            if v not in dic:
                dic[v]=k
        ans=[]
        for item in nums:
            ans.append(dic[item])
        return ans
            
            