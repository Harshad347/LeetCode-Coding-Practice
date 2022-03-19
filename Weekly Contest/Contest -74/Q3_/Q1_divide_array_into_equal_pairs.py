class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # if len is odd then we cant divide into pairs
        if len(nums) % 2 != 0:
            return False
        else:
            nums.sort()
            i = 0
            while i < len(nums):
                # counting frequency of element
                freq = nums.count(nums[i])
                # if frequency is odd, we can't make pairs
                if freq % 2 != 0:
                    return False
                else:
                    i = i+freq

            return True
