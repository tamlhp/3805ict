def lcs(X, Y):
    # Lengths of sequences
    m = len(X)
    n = len(Y)
    
    # Create the DP table with (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS from the DP table
    lcs_sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_sequence.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs_sequence.reverse()  # Because we've built it backwards
    return lcs_sequence

# Sequences
X = [1, 0, 0, 1, 0, 1, 0, 1]
Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

# Compute LCS
result = lcs(X, Y)
print(result)
