def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def dynamic_programming_paths(n):
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][n-1]

# Board size
board_size = 8

# Dynamic Programming Approach
dp_result = dynamic_programming_paths(board_size)

# Combinatorial Approach
combinatorial_result = comb(2 * (board_size - 1), board_size - 1)

dp_result, combinatorial_result