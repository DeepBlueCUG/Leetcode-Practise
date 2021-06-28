#有效括号，这个与栈有关，比较简单
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for element in s:

            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            else:
                if len(stack) == 0:
                    return False
                target = stack.pop()
                if (target == '(' and element == ')') or \
                    (target == '[' and element == ']') or\
                    (target == '{' and element == '}'):
                    continue
                else:
                    return False

        if len(stack) != 0:
            return False
        else:
            return True

solution_test = Solution()
result = solution_test.isValid(')')
print(result)
