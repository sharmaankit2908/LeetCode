class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Method 1
        # Time Complexity of O(n*n)
        # Space Complexity of O(1)
        # nums=arr
        # ans=[-1]*len(nums)
        # for i in range(len(nums)-1):
        #     a=max(nums[i+1:])
        #     ans[i]=a
        # return ans
        
        
        # Method 2
        # Time Complexity of O(n)
        nums=arr
        n=len(nums)
        if n==1:
            return [-1]
        if n==0:
            return []
        
        ans=[-1]*n
        ans[-2]=nums[-1]
        maxi=nums[-1]
        for i in range(n-2,-1,-1):
            maxi=max(maxi,nums[i+1])
            ans[i]=maxi
        return ans
            