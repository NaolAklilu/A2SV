# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = ListNode()
        
        heap = []
        head = ListNode()
        for linkedList in lists:
            while linkedList:
                head.next = linkedList
                heap.append(head.val)
                linkedList = linkedList.next
                head = head.next
        heap.append(head.val)
        heappop(heap)
        heapify(heap)

        temp = dummyNode
        while heap:
            num = heappop(heap)
            temp.next = ListNode(val=num)
            temp = temp.next
        
        return dummyNode.next