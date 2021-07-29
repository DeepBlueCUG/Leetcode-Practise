#二分查找
class Solution:
    def search(self, nums: list, target: int) -> int:

        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                # 最关键的就是这个左右指针的加一和减一，如果不这么作，左右指针出现相邻的位置之后middle就永远是left+1
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        return result

solution = Solution()
result = solution.search([-1, 0, 3, 5, 9, 12], 2)
print(result)


