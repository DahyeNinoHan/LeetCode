class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        current_new = dummy
        current = head.next
        sum_value = 0
        
        while current is not None:
            if current.val != 0:
                sum_value += current.val
            else:
                if sum_value != 0:
                    current_new.next = ListNode(sum_value)
                    current_new = current_new.next
                    sum_value = 0
            current = current.next
        
        return dummy.next