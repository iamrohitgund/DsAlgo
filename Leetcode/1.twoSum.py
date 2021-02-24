class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iMap = { }  #val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in iMap:
                return [iMap[diff],i]
            iMap[n] = i
        return 

#Time and Space O(n)