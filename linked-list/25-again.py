# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail_anterior = dummy
        can = True

        while can:
            ## verify if has next k elements
            ## verify if needs to be inverted
            i = 0
            node = head

            while node and i < k:
                node = node.next
                i+=1
            
            if i < k:
                can = False
                break

            i = 0
            prev = None
            while i < k:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
                i += 1
            

            new = tail_anterior.next
            tail_anterior.next = prev
            new.next = head
            tail_anterior = new
            
        return dummy.next