# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class List:
    def creat_list(self, nums: list) -> ListNode:
        if not nums:
            return None
        head = ListNode(nums.pop(0))
        current_node = head
        for element in nums:
            current_node.next = ListNode(element)
            current_node = current_node.next
        return head


def traverse_list(head: ListNode):
    if not head:
        return None
    print(head.val)
    if head.next:
        traverse_list(head.next)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            reverse_head = self.reverseList(head.next)
            #这应该是摘掉当前连接反转列表的做法
            head.next.next = head
            head.next = None

            return reverse_head

link = List().creat_list([])
traverse_list(link)
solution = Solution()
reverse_link = solution.reverseList(link)
traverse_list(reverse_link)