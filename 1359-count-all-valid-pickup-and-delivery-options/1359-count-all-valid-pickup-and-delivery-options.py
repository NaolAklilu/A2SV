class Solution:
    def countOrders(self, n: int) -> int:
        modulo = 10**9 + 7
        return (math.factorial(2*n) // (2**n))%modulo