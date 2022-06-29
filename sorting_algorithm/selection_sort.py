
# Best	O(n2)
# Worst	O(n2)
# Average	O(n2)
# Space Complexity	O(1)
# Stability	No

def selection_sort(item_list):
    """Selection sort algorithm with Python"""
    for i in range(len(item_list) - 1):
        min_position = i
        for j in range(i, len(item_list)):
            if item_list[j] < item_list[min_position]:
                min_position = j
        item_list[i], item_list[min_position] = item_list[min_position], item_list[i]                        

item_list = [3,2,-2,6,3,5,-8,32,5,4]
selection_sort(item_list)
print(item_list)

# Output : [-8, -2, 2, 3, 3, 4, 5, 5, 6, 32]