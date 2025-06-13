#!/usr/bin/python3


def makeChange(coins, total):
    """Make change with fewest coins"""
    if total <= 0:
        return 0

    # Initialize DP array with "infinite" (more than total)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins needed to make total 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
