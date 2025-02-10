#21. Merge Two Sorted Lists
#this is a YouTube based solution 
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
        
        

      
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ll=list1
        kk=list2
        
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
        self.print_list(dummy.next)
        return dummy.next
    
    def print_list(self,List):
        current_node= List
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print(None)
        

        

def main():
    
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next=l2

    l3 = ListNode(4,None)
    l2.next=l3

    
    k1 = ListNode(1)
    
    k2 = ListNode(3)
    k1.next=k2
    k3 = ListNode(4,None)
    k2.next=k3
    
    
    solution = Solution()
    solution.mergeTwoLists(l1,k1)
    
main()