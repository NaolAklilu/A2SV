# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list1head = list1
        list2head = list2
        
        dummyNode = ListNode()
        temp = dummyNode
        
        while list1head != None and list2head != None:
            if list1head.val <= list2head.val:
                temp.next = list1head
                list1head = list1head.next
            else:
                temp.next = list2head
                list2head = list2head.next
                
            temp = temp.next

        
        if list1head != None:
            temp.next = list1head
                
        elif list2head != None:
            temp.next = list2head
            
        head = dummyNode.next
        return head