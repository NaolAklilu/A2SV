class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a table to store the minimum number of coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # We can make up 0 amount with 0 coins

        # For each coin in the array
        for coin in coins:
            # For each amount from the coin value to the target amount
            for x in range(coin, amount + 1):
                # If making up this amount with this coin is less than making up the amount without this coin
                if dp[x - coin] + 1 < dp[x]:
                    # Update the table
                    dp[x] = dp[x - coin] + 1

        # If we can't make up the target amount, return -1
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]