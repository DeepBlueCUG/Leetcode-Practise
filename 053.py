#使用分治法联系053归并排序问题
#这里的分治思想是按照中间位置把列表分为左子列和右子列来处理
#题目就转化成了穿过中间点和不穿中间点两种情况
#穿中间点的话：
#那么就是左子列中以右端为起点的最大子列，右子列中以左端为起点的最大子列和这两种情况相加一共三种情况
#如果不穿中间点，就是左子列的最大子列，右子列的最大子列两种情况
class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            middle = len(nums) // 2

            #如果最大子段不穿过中间位置，则可能地最大子段和：
            sum_whole_left = self.maxSubArray(nums[0: middle])
            sum_whole_right = self.maxSubArray(nums[middle: len(nums)])

            #如果最大子段穿过中间位置，则可能地最大子段和为：
            max_left = nums[middle - 1]
            for i in range(middle - 1, -1, -1):
                temp = nums[i: middle]
                max_left = max(max_left, sum(nums[i: middle]))
            max_right = nums[middle]
            for i in range(middle + 1, len(nums)):
                temp2 = nums[middle: i + 1]
                max_right = max(max_right, sum(nums[middle: i + 1]))

            sum_middle = max(max_left, max_right, max_left + max_right)

            return max(sum_whole_left, sum_whole_right, sum_middle)

        # max_sum = nums[0]
        # for i in range(1, len(nums) + 1):
        #     for j in range(len(nums) - i + 1):
        #         sub_nums = nums[j: j + i]
        #         max_sum = max(max_sum, sum(sub_nums))
        # return max_sum

solution = Solution()
result = solution.maxSubArray([5, 4, -1, 7, 8])
print(result)
