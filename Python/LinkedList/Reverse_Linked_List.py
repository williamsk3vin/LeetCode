class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        
        return prev
