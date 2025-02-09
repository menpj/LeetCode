#141. Linked List Cycle
#My solution YouTube Inspired
# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodelist=[]
        node=head
        while head:
            if node in nodelist:
                #print("there is a cycle")
                return True
                

            else:
                if node.next==None:
                
                    return False
                else:
                    #print("infinu")
                    nodelist.append(node)
                    node=node.next
        #print("exit")
        #return False