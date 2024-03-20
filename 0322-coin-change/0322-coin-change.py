class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a cache to avoid redundant computation
        cache = dict()

        def dp(x):
            # Base case: if the amount is 0, return 0 coins
            if x == 0:
                return 0
            # If the amount is not in the cache, compute it and store it in the cache
            if x not in cache:
                # Initialize the minimum number of coins to infinity
                min_coins = float('inf')
                # For each coin in the array
                for coin in coins:
                    # If the coin is less than or equal to the amount
                    if coin <= x:
                        # Calculate the minimum number of coins for the remaining amount
                        min_remaining_coins = dp(x - coin)
                        # If the remaining amount can be made up with fewer coins than the current minimum
                        if min_remaining_coins != -1 and min_remaining_coins + 1 < min_coins:
                            # Update the minimum number of coins
                            min_coins = min_remaining_coins + 1
                # If no combination of coins can make up the amount, return -1
                if min_coins == float('inf'):
                    cache[x] = -1
                else:
                    cache[x] = min_coins
            # Return the minimum number of coins for the amount from the cache
            return cache[x]

        # Call the dp function with the target amount
        return dp(amount)