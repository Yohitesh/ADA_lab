def knapsack(weights, values, capacity):
    n = len(values)
    
    # Create a 2D DP table
    dp = []
    for i in range(n + 1):
        row = []
        for j in range(capacity + 1):
            row.append(0)
        dp.append(row)

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Max of including the item or excluding it
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # If weight is more than capacity, don't include item
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)
