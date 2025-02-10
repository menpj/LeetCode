#21. Merge Two Sorted Lists
 
# Definition for singly-linked list.
#not working
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
        kk=list1
        ll=list2
        
        
        head=ll
        if ll and kk:
            if ll.val <= kk.val:
                ll=ll.next
            else:
                temp=head
                head=kk
                kk=kk.next
        elif kk:
            temp=head
            head=kk
            kk=kk.next
        elif ll:
            temp = ListNode(ll.val)
            m.next=temp
            m=m.next
            ll=ll.next
        #m=ListNode()
        while ll or kk:
            if ll and kk:
                if ll.val <= kk.val:
                    current=ll
                    ll=ll.next
                else:
                    temp=current
                    current=
                    current.next=temp
                    m=m.next
                    kk=kk.next
            elif kk:
                temp = ListNode(kk.val)
                m.next=temp
                m=m.next
                kk=kk.next
            elif ll:
                temp = ListNode(ll.val)
                m.next=temp
                m=m.next
                ll=ll.next
            else:
                break
        
        #merged.print_list()
        self.print_list(head)
        return head
    
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