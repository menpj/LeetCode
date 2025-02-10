#21. Merge Two Sorted Lists
#this is not the solution this won't work
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next= new_node
        
    def print_list(self):
        current_node= self.head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")
            
        
      
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ll=list1.head
        kk=list2.head
        merged = LinkedList()
        
        while ll or kk:
            if ll and kk:
                if ll.val <= kk.val:
                    merged.append(ll.val)
                    ll=ll.next
                else:
                    merged.append(kk.val)
                    kk=kk.next
            elif kk:
                merged.append(kk.val)
                kk=kk.next
            elif ll:
                merged.append(ll.val)
                ll=ll.next
            else:
                break
        
        #merged.print_list()
        return merged

        

def main():
    
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(6)
    ll.print_list()
    
    kk = LinkedList()
    kk.append(2)
    kk.append(4)
    kk.append(5)
    kk.print_list()
    
    solution = Solution()
    solution.mergeTwoLists(ll,kk)
    
main()