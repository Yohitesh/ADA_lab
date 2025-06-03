import time

# Quick Sort function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Input
n = int(input("Enter number of elements: "))
arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

# Time calculation
start_time = time.time()

sorted_arr = quick_sort(arr)

end_time = time.time()
time_taken = end_time - start_time

# Output
print("\nSorted array:")
print(sorted_arr)

print(f"\nTime taken by Quick Sort: {time_taken:.6f} seconds")
