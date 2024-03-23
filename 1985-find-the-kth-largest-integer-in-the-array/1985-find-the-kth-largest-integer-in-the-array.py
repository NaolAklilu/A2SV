class Solution:
    def kthLargestNumber(self, arr: List[str], k: int) -> str:
        arr = list(map(int, arr))
        arr.sort(reverse=True)
        return str(arr[k-1])