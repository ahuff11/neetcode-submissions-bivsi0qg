# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast and slow pointer again i think to find middle and end
        # we need to reverse the list for the slow pointer, then if 
        dummy = ListNode(0, head)
        left = dummy
        right = head
        count = 0
        while count < n:
            right = right.next
            count +=1
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        left = left.next

        return dummy.next
