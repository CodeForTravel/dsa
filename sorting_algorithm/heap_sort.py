# # Heap Sort in python

# Best	O(nlog n)
# Worst	O(nlog n)
# Average	O(nlog n)
# Space Complexity	O(1)
# Stability	No

# In binary tree array representation, if 'i' is the index of root, then his 
#left child index will be : 2*i + 1
#right child index will be : 2*i + 2

def heapify(arr, arr_lenght, current_index):
    # Find largest among root and children
    largest_node_index = current_index # let
    left_node_index = 2 * current_index + 1
    right_node_index = 2 * current_index + 2

    if left_node_index < arr_lenght and arr[left_node_index] > arr[current_index]:
        largest_node_index = left_node_index

    if right_node_index < arr_lenght and arr[right_node_index] > arr[largest_node_index]:
        largest_node_index = right_node_index

    # If root is not largest, swap with largest and continue heapifying
    if largest_node_index != current_index:
        arr[current_index], arr[largest_node_index] = arr[largest_node_index], arr[current_index]
        heapify(arr, arr_lenght, largest_node_index)


def heap_sort(arr):
    arr_length = len(arr)

    # make the array as max heap
    for i in range(arr_length//2, -1, -1):
        heapify(arr, arr_length, i)

    # sort the array with heap_sort
    for i in range(arr_length-1, 0, -1):
        # swaping the last element with first element of array
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)

arr = [1, 12, 9, 34, 23, 56, 5, 6, 10]
print(f"list before sort: {arr}")
heap_sort(arr)
print(f"list after sort: {arr}")

# Simple procedure:
# heapify the given array
# apply heap sort

# after heapify and building max heap, height element will be at 0th position

# swap the first element with last element 
# again hepify the array from 0 till last swapped element

# repeat the above procedure