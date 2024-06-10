def optimal_bst(p, q, n):
    # Create tables for costs and roots
    e = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    w = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Base cases: single keys
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    # Construct the e and root tables
    for length in range(1, n + 1):  # length of the chain
        for i in range(1, n - length + 2):  # starting index
            j = i + length - 1  # ending index
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j] + q[j]

            # Find the optimal root for trees spanning from i to j
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e, root

# Given probabilities
p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]  # p[0] is a dummy, actual starts from p[1]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]

# Number of keys
n = 7

# Calculate optimal BST
cost, roots = optimal_bst(p, q, n)

# Display the cost of the optimal BST
optimal_cost = cost[1][n]
print("Cost of the Optimal Binary Search Tree is:", optimal_cost)
print("Roots table:")
for row in roots[1:n+1]:
    print(row[1:n+1])
