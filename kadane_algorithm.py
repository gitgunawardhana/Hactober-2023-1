def kadane_algorithm(arr):
    max_so_far = float('-inf')
    max_ending_here = 0

    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum = kadane_algorithm(arr)
print("Maximum subarray sum:", max_subarray_sum)
