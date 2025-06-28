#!/usr/bin/python3
"""
Prime Game
"""


def sieve(n):
    """Return a list with the number of primes up to and including n"""
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Count the number of primes up to index i
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    return prime_count


def isWinner(x, nums):
    """
    Determines the winner of each game round
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_count = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
