def is_interleaving(A, B, C):
    M, N = len(A), len(B)

    # If the length of C is not equal to the sum of A and B, then C cannot be an interleaving
    if len(C) != M + N:
        return False

    # Create a 2D table to store solutions to subproblems
    dp = [[False] * (N + 1) for _ in range(M + 1)]

    # Initialize dp[0][0] as True
    dp[0][0] = True

    # Fill the first row: A is empty, so each cell depends on previous cell in the row and matching character in B
    for j in range(1, N + 1):
        dp[0][j] = dp[0][j - 1] and B[j - 1] == C[j - 1]

    # Fill the first column: B is empty, so each cell depends on previous cell in the column and matching character in A
    for i in range(1, M + 1):
        dp[i][0] = dp[i - 1][0] and A[i - 1] == C[i - 1]

    # Fill the rest of dp table
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            dp[i][j] = (dp[i - 1][j] and A[i - 1] == C[i + j - 1]) or (dp[i][j - 1] and B[j - 1] == C[i + j - 1])

    return dp[M][N]

# Example usage:
A = "ABC"
B = "ACD"
C = "AACBCD"
result = is_interleaving(A, B, C)
print("Is interleaving:", result)
