def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        
        # If the target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If the target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If the target is not present in the array
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)

if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found in the array")
