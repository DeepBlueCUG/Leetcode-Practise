# Definition for singly-linked list.
class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Link:

    def creat_link(self, nums: list) -> LinkNode:
        root_node = LinkNode(None)
        current_node = root_node
        for element in nums:
            current_node.next = LinkNode(element)
            current_node = current_node.next
        return root_node.next


def traverse_link(linknode: LinkNode):
    if linknode:
        print(linknode.val)
        next_linknode = linknode.next
        traverse_link(next_linknode)
    else:
        return


class Solution:
    def mergeTwoLists(self, l1: LinkNode, l2: LinkNode) -> LinkNode:

        #肯定还是迭代法时间复杂度比较低
        result = LinkNode(None)
        current_linknode = result

        while l1:

            #此时l1和l2都存在
            if l2:
                min_val = min(l1.val, l2.val)
                current_linknode.next = LinkNode(min_val)
                current_linknode = current_linknode.next
                if l1.val == min_val:
                    l1 = l1.next
                else:
                    l2 = l2.next
            #此时只有l1
            else:
                current_linknode.next = l1
                break

        #还有一种只有l2的情况
        if l2:
            current_linknode.next = l2

        return result.next

l1_test = Link()
l2_test = Link()
l1_test = l1_test.creat_link([1])
l2_test = l2_test.creat_link([])
# traverse_link(l1_test.root_linknode)
# traverse_link(l2_test.root_linknode)
resolution_test = Solution()
result = resolution_test.mergeTwoLists(l1_test, l2_test)
traverse_link(result)