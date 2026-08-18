# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop until both lists are exhausted and there is no carry left
        while l1 is not None or l2 is not None or carry != 0:
            # Get the values from the current nodes, or 0 if we've reached the end of a list
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the digit part of the sum
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummy_head.next