class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        while head:
            array.append(head.val)
            head = head.next
            
        for i in range(len(array) // 2):
            if array[i] != array[len(array) - 1 - i]:
                return False
            
        return True