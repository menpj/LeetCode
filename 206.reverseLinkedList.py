# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if head:
            slow=head
        else:
            #print("retuening")
            return    
        if head.next:
            fast=head.next
        else:
            #print(retuening)
            return head
        
        tfn=fast.next
        fast.next=slow
        slow.next=None
        
        
        slow=fast
        fast=tfn
        
        while slow and fast:
            tfn=fast.next
            fast.next=slow
            slow=fast
            fast=tfn
        
        head=slow
        self.print_list(head)
        return slow
            
        
        

    def print_list(self,head):
        current_node= head
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

    
   
    
    
    solution = Solution()
    solution.reverseList(l1)
    
main()