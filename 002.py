#两数相加

#首先构造链表
class LinkNode:
    def __init__(self, element):
        self.val = element
        self.next = None

#特别注意这个写法是不行的。python的类都是基类，如果直接改写属性的话实例化之后这个属性跟着就会呗改变
#正确的写法参照021题
class Link:

    root_node = LinkNode(None)#起始根节点没有值

    def __init__(self, num_list: list):

        current_node = self.root_node

        for element in num_list:
            current_node.next = LinkNode(element)
            current_node = current_node.next

        self.root_node = self.root_node.next

def travers_link(link_node: LinkNode):
    if link_node:
        print(link_node.val)
        travers_link(link_node.next)

# #迭代法
# class Solution:
#     def addTwoNumbers(self, l1: LinkNode, l2: LinkNode) -> LinkNode:
#
#         total = 0
#         #如果需要进位那么进位值用remain储存
#         remain = 0
#         root_node = LinkNode(None)
#         current_node = root_node
#
#         #同时迭代两个列表，讲节点值相加
#         while l1 and l2:
#             total = l1.val + l2.val + remain
#             current_node.next = LinkNode(total % 10)
#             current_node = current_node.next
#             remain = total // 10
#             l1 = l1.next
#             l2 = l2.next
#
#         #处理一个列表有节点另一个没有的情况
#         while l1 and l2 is None:
#             total = l1.val + remain
#             current_node.next = LinkNode(total % 10)
#             current_node = current_node.next
#             remain = total // 10
#             l1 = l1.next
#
#         while l2 and l1 is None:
#             total = l2.val + remain
#             current_node.next = LinkNode(total % 10)
#             current_node = current_node.next
#             remain = total // 10
#             l2 = l2.next
#
#         #判断一下最后如果还有进位值剩余的情况
#         if remain:
#             current_node.next = LinkNode(remain)
#
#         #根节点没有值，所以返回root_node的下一个节点作为根节点
#         return root_node.next


#递归法
class Solution:
    def addTwoNumbers(self, l1: LinkNode, l2: LinkNode) -> LinkNode:

        total = l1.val + l2.val
        remain = total // 10
        current_node = LinkNode(total % 10)
        l1 = l1.next
        l2 = l2.next

        if l1 and l2:
            l1.val = l1.val + remain
            current_node.next = self.addTwoNumbers(l1, l2)
        elif l1 and l2 is None:
            l2 = LinkNode(0)
            l1.val = l1.val + remain
            current_node.next = self.addTwoNumbers(l1, l2)
        elif l2 and l1 is None:
            l1 = LinkNode(0)
            l1.val = l1.val + remain
            current_node.next = self.addTwoNumbers(l1, l2)
        else:
            if remain > 0:
                current_node.next = LinkNode(remain)

        return current_node


link_1 = Link([9, 9, 9, 9, 9, 9, 9])
link_2 = Link([9, 9, 9, 9])
resolution_test = Solution()
result = resolution_test.addTwoNumbers(link_1.root_node, link_2.root_node)
travers_link(result)









