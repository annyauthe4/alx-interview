In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

<h1> Problem Breakdown</h1>
Each time you:

Copy All = 1 operation

Paste = 1 operation

The key observation is:

To reach n Hs, you can only copy a group of x Hs and paste it k times such that x * k = n.

So, the minimal number of operations to reach n is the sum of its prime factors.

Optimal Approach: Prime Factorization
For every factor i of n, the minimum number of operations is:

Solve for n // i, and add i operations (1 Copy All + (i-1) Pastes).

So we iteratively divide n by its smallest factor and accumulate the operations.
