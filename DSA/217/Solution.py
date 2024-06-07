class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        hashset = set()
        for n in nums:
            if n in hashset :
                return True
            hashset.add(n)
        return False        