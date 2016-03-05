# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        cur1 = l1
        cur2 = l2
        prev1 = l1
        prev2 = l2
        
        if cur1 is None or cur2 is None:
            return
        
        while cur1 is not None and cur2 is not None:
            cur1.val += cur2.val
            if cur1.val >= 10:
                cur1.val -= 10
                if cur1.next is not None:
                    cur1.next.val += 1
                else:
                    cur1.next = ListNode(1)
            prev1 = cur1
            prev2 = cur2
            cur1 = cur1.next
            cur2 = cur2.next
        
        if cur1 is None:
            prev1.next = prev2.next 
        return l1
            
