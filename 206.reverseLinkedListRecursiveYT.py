#https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#YT SOLUTION ideal solution, cleaner and better than mine
#https://www.youtube.com/watch?v=G0_I-ZF0S38
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
        
        if not head:
            return None
        newhead=head
        if head.next:
            newhead= self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return newhead
            
        
        

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
    head=solution.reverseList(l1)
    solution.print_list(head)
main()