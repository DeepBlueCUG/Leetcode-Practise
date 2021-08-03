# 定长数组可以使用滑动窗口方法来做
class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:

        for i in range(1, len(nums) + 1):
            sum = 0
            for j in range(i):
                sum = sum + nums[j]
                if sum >= target:
                    return i
            for j in range(1, len(nums) - i + 1):
                sum = sum - nums[j - 1] + nums[j + i - 1]
                if sum >= target:
                    return i

        return 0

solution = Solution()
result = solution.minSubArrayLen(11, [1, 2, 3, 4, 5])
print(result)


