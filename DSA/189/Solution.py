class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # for _ in range(k):
        #     temp = nums[-1]
        #     for n in range(len(nums)):
        #         swap = nums[n] 
        #         nums[n] = temp
        #         temp = swap
        # return nums

        
        k = k % len(nums)
        if k > 0:
            self.reverse(nums,0,len(nums)-1)
            self.reverse(nums,0,k-1)
            self.reverse(nums,k,len(nums)-1)

    def reverse(self,nums,i,j):
            while i < j :
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp 
                i = i + 1
                j = j - 1