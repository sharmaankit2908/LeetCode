class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Method 1 
        # Time complexity of O(n)
        # ans=[]
        # n=len(nums)
        # for i in range(len(nums)):
        #     if nums[i]%2==0:
        #         ans.append(nums[i])
        # for i in range(len(nums)):
        #     if nums[i]%2!=0:
        #         ans.append(nums[i])
        # return ans
        
        # Method 1 with different Code
        return [i for i in nums if i%2==0] + [i for i in nums if i%2 !=0]