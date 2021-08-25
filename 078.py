#尝试使用回溯法解决
class Solution:
    def subsets(self, nums: list) -> list:
        if len(nums) == 0:
            return []
        else:
            temp = []
            result = []
            current_index = 0
            self.__recall(nums, current_index, temp, result)
            return result

    # 开头单下划线约定该函数为内部使用
    # 如果实际参数的数据类型是可变对象（列表、字典），则函数参数的传递方式将采用引用传递方式
    # 函数会直接修改result的值，因此不需要返回
    # 注意普通变量是传值操作，函数内的操作不会修改原变量的值
    def __recall(self, nums: list, current_index, temp: list, result: list):
        result.append(temp[:]) # 如果只传temp，是传址操作，会把所有result的子集更改
        for i in range(current_index, len(nums)):
            temp.append(nums[i])
            self.__recall(nums, i + 1, temp, result)
            temp.pop()

solution = Solution()
result = solution.subsets([1, 2, 3])
print(result)




