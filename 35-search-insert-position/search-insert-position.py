class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0 
        e = len(nums)
        mid = 0
        while s < e:
            mid = s+(e-s)//2
            if target == nums[mid] :
                return mid
            elif target < nums[mid]:
                e = mid
            else:
                s = mid +1
        return s
       