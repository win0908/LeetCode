class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        '''
        #Time: O(n)
        for i in range(len(nums)):
            if nums[i] == target: return i
            if nums[i] > target:  return i

        return len(nums)
        '''

        
        #Time: O(log n)
        #Space: O(1)
        
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l
        
