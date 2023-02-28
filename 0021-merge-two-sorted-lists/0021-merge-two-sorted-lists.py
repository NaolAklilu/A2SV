# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge_helper(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.merge_helper(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_helper(list1, list2.next)
            return list2
    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = self.merge_helper(list1, list2)
        
        return dummyNode.next