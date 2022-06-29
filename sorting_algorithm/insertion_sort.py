# Best	O(n)
# Worst	O(n2)
# Average	O(n2)
# Space Complexity	O(1)
# Stability	Yes


def insertion_sort(item_list):
    """Insertion sort algorithm with Python"""
    for i in range(1, len(item_list) -1):
        item = item_list[i]
        j = i-1
        while j >= 0 and item < item_list[j]:
            item_list[j+1] = item_list[j]
            j -= 1
        item_list[j+1] = item


item_list = [3,2,-2,6,3,5,-8,32,5,4]
insertion_sort(item_list)
print(item_list)

# Output : [-8, -2, 2, 3, 3, 4, 5, 5, 6, 32]