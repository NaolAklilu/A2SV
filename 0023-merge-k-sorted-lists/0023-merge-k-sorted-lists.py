# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a heap with the first node of each list
        heap = [(node.val, idx) for idx, node in enumerate(lists) if node]
        heapq.heapify(heap)

        # Initialize the head of the result list
        head = point = ListNode()

        while heap:
            val, idx = heapq.heappop(heap)
            point.next = ListNode(val)
            point = point.next

            # If there is a next node in the list, add it to the heap
            if lists[idx].next:
                heapq.heappush(heap, (lists[idx].next.val, idx))
                lists[idx] = lists[idx].next

        return head.next
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    
        