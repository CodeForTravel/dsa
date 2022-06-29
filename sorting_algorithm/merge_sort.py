# MergeSort in Python
# Best	O(n*log n)
# Worst	O(n*log n)
# Average	O(n*log n)
# Space Complexity	O(n)
# Stability	Yes

def merge_sort(item_list):
    """Merge sort algorithm with Python"""
    if len(item_list) > 1:
        mid = len(item_list)//2
        left_list = item_list[:mid]
        right_list = item_list[mid:]

        # sorting divided list
        merge_sort(left_list)
        merge_sort(right_list)

        i= j = k = 0

        # Until we reach either end of either left_list or right_list, pick larger among
        # elements left_list and right_list and place them in the correct position at A[p..r]
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                item_list[k] = left_list[i]
                i += 1
            else:
                item_list[k] = right_list[j]
                j += 1
            k += 1

        # When we run out of elements in either left_list or right_list,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left_list):
            item_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            item_list[k] = right_list[j]
            j += 1
            k += 1

        

item_list = [3,2,-2,6,3,5,-8,32,5,4]
merge_sort(item_list)
print(item_list)