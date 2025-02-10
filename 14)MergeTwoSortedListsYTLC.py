# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, ll, kk):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
       
        
        dummy = ListNode()
        tail=dummy
        #m=ListNode()
        while ll and kk:
            
            if ll.val <= kk.val:
                
                tail.next = ll
                ll=ll.next
            else:
                
                tail.next=kk
                kk=kk.next
            tail=tail.next
        if kk:
            tail.next=kk
        elif ll:
            tail.next=ll
    
        
        #merged.print_list()
        #self.print_list(dummy.next)
        return dummy.next