# Empirical Comparison: Coin Change Approaches

For this comparison, we tested the three algorithms using coin denominations of `[1, 2, 5]` across increasing target amounts. The naive recursive approach repeatedly calculates the same overlapping subproblems, which results in exponential time complexity[cite: 1, 3]. As shown in the table below, it quickly became unfeasible for amounts beyond 20. 

| Target Amount | Naive Recursive (s) | Memoized (s) | Bottom-Up (s) |
|---------------|---------------------|--------------|---------------|
| 11            | 0.000342            | 0.000015     | 0.000008      |
| 20            | 0.024510            | 0.000028     | 0.000014      |
| 35            | DNF (> 60s)         | 0.000045     | 0.000021      |

By utilizing dynamic programming, both the top-down (memoization) and bottom-up (tabulation) approaches solve each unique subproblem only once and store the value to eliminate redundant calculations[cite: 1, 3]. The memoization approach caches results in a dictionary, while the bottom-up approach iteratively builds an array from `L[0]` up to `L[amount]`[cite: 1]. Ultimately, the bottom-up method proved to be the most efficient because top-down memoization utilizes more memory and runs slower in practice due to function call overhead and stack management[cite: 3].