class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        #   Method 1
        target=[]
        n=len(nums)
        for i in range(n):
            target.insert(index[i],nums[i])
        return target
