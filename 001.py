#两数之和
class Solution:
    def twoSum(self, nums: list, target) -> list:

        result = []
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = i
        for j in range(len(nums)):
            diff = target - nums[j]
            if map.__contains__(diff) and map.get(diff) != j:
                result.append(j)
                result.append(map.get(diff))
                return result

        return result

solution_test = Solution()
result_test = solution_test.twoSum([2, 7, 11, 15], 9)
print(result_test)