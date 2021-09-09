# 救生艇，双指针解决
# 条件中指明(保证每个人都能被船载)，说明不存在单人超载的可能性
# 对撞指针的思路是对的，如果最轻的不能和最重的一起乘船，那么最重的只能单人乘船
# 如果可以，他们俩人一条船
class Solution:
    def numRescueBoats(self, people: list, limit: int) -> int:

        # 这个题在使用双指针前必须先排序了
        people.sort()
        num_boat = 0
        light = len(0)
        heavy = len(people) - 1

        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            num_boat += 1

        return num_boat



solution = Solution()
result = solution.numRescueBoats([3, 8, 7, 1, 4], 9)
print(result)