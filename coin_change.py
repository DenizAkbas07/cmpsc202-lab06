import time
import sys

# Phase 1: Naive Recursive Approach
def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        res = coin_change_recursive(coins, amount - coin)
        if res != float('inf'):
            min_coins = min(min_coins, 1 + res)
            
    return min_coins

# Phase 2: Top-Down DP (Memoization)
def coin_change_memoized(coins, amount, memo=None):
    if memo is None:
        memo = {}
        
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    if amount in memo:
        return memo[amount]
        
    min_coins = float('inf')
    for coin in coins:
        res = coin_change_memoized(coins, amount - coin, memo)
        if res != float('inf'):
            min_coins = min(min_coins, 1 + res)
            
    memo[amount] = min_coins
    return min_coins

# Phase 3: Bottom-Up DP (Tabulation)
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount]

# Phase 4: Empirical Comparison Script
if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    
    coins = [1, 2, 5]
    test_amounts = [11, 20, 35]
    
    print(f"{'Amount':<10} | {'Recursive (s)':<15} | {'Memoized (s)':<15} | {'Bottom-Up (s)':<15}")
    print("-" * 65)
    
    for amount in test_amounts:
        # Recursive (skipped for 35 to avoid hanging)
        if amount <= 20:
            start = time.perf_counter()
            coin_change_recursive(coins, amount)
            rec_time = time.perf_counter() - start
        else:
            rec_time = float('inf')
            
        # Memoized
        start = time.perf_counter()
        coin_change_memoized(coins, amount)
        memo_time = time.perf_counter() - start
        
        # Bottom-Up
        start = time.perf_counter()
        coin_change_dp(coins, amount)
        dp_time = time.perf_counter() - start
        
        rec_str = f"{rec_time:.6f}" if rec_time != float('inf') else "DNF (>60s)"
        print(f"{amount:<10} | {rec_str:<15} | {memo_time:<15.6f} | {dp_time:<15.6f}")