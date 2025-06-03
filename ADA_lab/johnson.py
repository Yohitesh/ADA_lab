def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def get_mobile_element(perm, direction):
    mobile = 0
    index = -1
    for i in range(len(perm)):
        # Check if the element can move in its direction
        if direction[i] == -1 and i > 0 and perm[i] > perm[i - 1]:
            if perm[i] > mobile:
                mobile = perm[i]
                index = i
        if direction[i] == 1 and i < len(perm) - 1 and perm[i] > perm[i + 1]:
            if perm[i] > mobile:
                mobile = perm[i]
                index = i
    return index

def johnson_trotter(n):
    # Initial setup
    perm = [i + 1 for i in range(n)]
    direction = [-1] * n  # All move LEFT initially (-1 = left, 1 = right)

    print(perm)

    for _ in range(1, factorial(n)):
        mobile_index = get_mobile_element(perm, direction)
        if mobile_index == -1:
            break

        # Find index to swap with
        swap_with = mobile_index + direction[mobile_index]
        # Swap values and directions
        perm[mobile_index], perm[swap_with] = perm[swap_with], perm[mobile_index]
        direction[mobile_index], direction[swap_with] = direction[swap_with], direction[mobile_index]

        # Update all directions greater than moved element
        moved_value = perm[swap_with]
        for i in range(n):
            if perm[i] > moved_value:
                direction[i] *= -1

        print(perm)

# Example usage:
johnson_trotter(4)
