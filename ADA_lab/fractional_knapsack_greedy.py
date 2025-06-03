def fractional_knapsack(values, weights, capacity):
    # Calculate value/weight ratio and pair with original value and weight
    items = []
    for i in range(len(values)):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_value = 0.0

    for ratio, value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    return total_value

# Example
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in knapsack: {max_value:.2f}")
