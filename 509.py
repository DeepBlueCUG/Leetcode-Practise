#以斐波那契数列体会递归的意义
class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        else:
            m = self.fib(n - 1) + self.fib(n - 2)
        return m

solution = Solution()
result = solution.fib(4)
print(result)
