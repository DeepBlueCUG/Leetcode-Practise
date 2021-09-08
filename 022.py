# 22题能否用用回溯完成呢
# 是不是有效的括号组合，可以通过左右括号来判定，左括号数量一定大于右括号
class Solution:
    def generateParenthesis(self, n: int) -> list:

        result = []
        temp = ''
        left = 0
        right = 0
        self.__recall(n, right, left, temp, result)
        return result

    def __recall(self, num, left, right, temp, result: list):
        if len(temp) == 2 * num:
            result.append(temp[:])
            return
        if left < num:
            temp = temp + '('
            self.__recall(num, left + 1, right, temp, result)
            temp = temp[:-1]
        if right < left:
            temp = temp + ')'
            self.__recall(num, left, right + 1, temp, result)
            temp = temp[:-1]

solution = Solution()
result = solution.generateParenthesis(3)
print(result)



