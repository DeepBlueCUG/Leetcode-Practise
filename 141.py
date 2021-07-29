# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def creat_list(self, array: list, pos):
        head = ListNode(array[0])
        current_node = head
        if pos == 0:
            pos_node = current_node
        for i in range(1, len(array)):
            current_node.next = ListNode(array[i])
            current_node = current_node.next
            if i == pos:
                pos_node = current_node
        if pos != -1:
            current_node.next = pos_node
        return head





def traves_list(head: ListNode):
    current_node = head
    while current_node:
        print(current_node.val)
        current_node = current_node.next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast != slow: #这可以直接判断两个指针是否指向了同一个节点
            if not fast or not fast.next: #如果节点后面为空，则说明该链没有坏
                return False
            else:
                fast = fast.next.next
            slow = slow.next
        return True

test_list = List()
test_list = test_list.creat_list([3, 2, 0, -4], 1)
#traves_list(test_list)
solution = Solution()
print(solution.hasCycle(test_list))
#遗留问题：如何写环链表呢？