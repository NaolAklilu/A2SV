class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        to_list, stack, i = [], [], 0
        while node:
            to_list.append(node.val)
            node = node.next
            
        res = [0] * len(to_list)
        while i < len(to_list):
            while stack and to_list[stack[-1]] < to_list[i]:
                res[stack.pop()] = to_list[i]
            stack.append(i)
            i+=1
            
        return res