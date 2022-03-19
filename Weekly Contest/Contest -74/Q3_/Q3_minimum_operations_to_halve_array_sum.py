# time limit exceeded

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        original_sum = float(sum(nums))

        latest_sum = original_sum
        steps = 0

        while latest_sum*2 >= original_sum:
            nums.sort()
            nums[-1] = float(nums[-1]/2)
            latest_sum = float(sum(nums))
            steps += 1

        return steps
