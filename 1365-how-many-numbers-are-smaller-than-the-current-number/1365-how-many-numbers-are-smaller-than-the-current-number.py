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
        # Time Complexity of O(nlogn)
        # dic={}
        # for k,v in enumerate(sorted(nums)):
        #     if v not in dic:
        #         dic[v]=k
        # ans=[]
        # for item in nums:
        #     ans.append(dic[item])
        # return ans
            
        # Method 3
        # Time Complexity of O(n)
        # m=max(nums)
        # dummy=[0]*(max(nums)+1)
        # n=len(nums)
        # for i in range(n):
        #     dummy[nums[i]] +=1
        # print(dummy)
        # for i in range(1,len(dummy)):
        #     dummy[i] +=dummy[i-1]
        # print(dummy)
        # ans=[]
        # for i in range(n):
        #     if nums[i] !=0:
        #         ans.append(dummy[nums[i]-1])
        #     else:
        #         ans.append(0)
        # return ans
        
        # Method 3 with different Code
        m=max(nums)
        dummy=[0]*(max(nums)+1)
        n=len(nums)
        for i in range(n):
            dummy[nums[i]] +=1
        print(dummy)
        for i in range(1,len(dummy)):
            dummy[i] +=dummy[i-1]
        print(dummy)
        ans=[0]*len(nums)
        for i in range(n):
            if nums[i] !=0:
                ans[i]=dummy[nums[i]-1]
        return ans
        