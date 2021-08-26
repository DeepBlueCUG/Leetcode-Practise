#回溯法练习2,看起来这个题的思路和78题几乎是一样的

class Solution:
    def combine(self, n: int, k: int) -> list:
        if n == 1:
            return [[1]]
        else:
            temp = []
            result = []
            self.__recall(n, k, 1, temp, result)
            return result

    def __recall(self, target, k, current_num, temp, result):
        for i in range(current_num, target + 1):
            temp.append(i)
            if len(temp) == k:
                result.append(temp[:])
            self.__recall(target, k, i + 1, temp, result)
            temp.pop() #回溯记录节点的话

solution = Solution()
result = solution.combine(4, 1)
print(result)
