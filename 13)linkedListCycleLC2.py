#141. Linked List Cycle
#YouTube Based solution
#https://www.youtube.com/watch?v=gBTe7lFR3vc
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow,fast=head,head
        
        while fast and fast.next:
                #print("there is a cycle")
                fast=fast.next.next
                slow=slow.next
                if fast==slow:
                    return True
                

    
        return False