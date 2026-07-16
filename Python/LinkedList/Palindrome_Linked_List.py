# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        left = head
        right = prev

        while left and right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True
