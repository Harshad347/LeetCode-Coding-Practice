# Time limit exceeded

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sum1 = float(sum(nums))
        latest_sum = sum1
        original_sum = sum1/2
        steps = 0

        while latest_sum >= original_sum:
            nums.sort()
            nums[-1] = float(nums[-1]/2)
            latest_sum = float(sum(nums))
            steps += 1

        return steps
