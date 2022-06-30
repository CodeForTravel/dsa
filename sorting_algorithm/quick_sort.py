# Quick sort with python
# Time Complexity	 
# Best	O(n*log n)
# Worst	O(n2)
# Average	O(n*log n)
# Space Complexity	O(log n)
# Stability	No


def quick_sort(arr, left, right):
    if left < right:
        pivot_position = partition(arr, left, right)
        quick_sort(arr, left, pivot_position-1)
        quick_sort(arr, pivot_position+1, right)


def partition(arr, left, right):
    i,j = left, right-1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > arr[right]:
        arr[i], arr[right] = arr[right], arr[i]

    return i


item_list = [3,2,-2,6,3,5,-8,32,5,4]
# item_list = []
print(f"Items before sort: {item_list}")
quick_sort(item_list, 0 , len(item_list)-1)
print(f"Items after sort: {item_list}")

# Output : [-8, -2, 2, 3, 3, 4, 5, 5, 6, 32]