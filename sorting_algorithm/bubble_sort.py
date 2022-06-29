# Best	O(n)
# Worst	O(n2)
# Average	O(n2)
# Space Complexity	O(1)
# Stability	Yes

def bublle_sort(list_):
    """Bubble sort algorithm with Python"""
    swapped =  False
    for i in range(len(list_) - 1):
        for j in range(len(list_) - 1 -i):
            if list_[j] > list_[j+1]:
                
                list_[j], list_[j+1] = list_[j+1], list_[j]
                swapped = True
        if not swapped:
            break


list_ = [3,2,-2,6,3,5,-8,32,5,4]
bublle_sort(list_)
print(list_)

# Output : [-8, -2, 2, 3, 3, 4, 5, 5, 6, 32]