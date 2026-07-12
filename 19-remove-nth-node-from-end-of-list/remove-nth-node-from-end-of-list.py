# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # fast pointer'ı n+1 adım öne taşı
        for _ in range(n + 1):
            fast = fast.next

        # fast sona ulaşana kadar ikisini birlikte ilerlet
        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next silinecek düğüm
        slow.next = slow.next.next
        return dummy.next
        