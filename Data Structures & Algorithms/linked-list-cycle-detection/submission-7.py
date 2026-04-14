# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowcurrent = head
        fastcurrent = head
        if head == None:
            return False
        while head.next is not None and fastcurrent:
            slowcurrent = slowcurrent.next
            fastcurrent = fastcurrent.next
            if fastcurrent == None:
                return False
            fastcurrent = fastcurrent.next
            if slowcurrent == fastcurrent and slowcurrent.next is not None:
                return True


        return False
        