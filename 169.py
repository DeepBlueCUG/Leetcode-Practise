# 169多数元素
# 练习使用分治法解决该问题
# 如何将整个问题拆解为更小的问题
class Solution:
    def majorityElement(self, nums: list) -> int:
        result = {}
        self.count_times_of_number(nums, result)
        for key, num in result.items():
            if num > int(len(nums) // 2):
                return key

    def count_times_of_number(self, current_list: list, result: dict):
        if len(current_list) > 1:

            next_first_half = current_list[: int(len(current_list) // 2)]
            self.count_times_of_number(next_first_half, result)
            next_second_half = current_list[int(len(current_list) // 2):]
            self.count_times_of_number(next_second_half, result)

        else:

            num = current_list[0]
            try:
                result[num] = result[num] + 1
            except:
                result[num] = 1

            return

solution = Solution()
result = solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
print(result)