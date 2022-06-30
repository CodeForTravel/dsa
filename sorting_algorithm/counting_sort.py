# # Counting sort in Python programming

def count_sort(item_list):
    list_size = len(item_list)
    output_list = [0] * list_size
    count_list = [0] * 10

    # store the count of each element in count list
    for i in range(0, list_size):
        count_list[item_list[i]] += 1

    # store the cummulative count in count list
    for i in range(1, 10):
        count_list[i] += count_list[i-1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = list_size - 1
    while i >= 0:
        output_list[count_list[item_list[i]] - 1] = item_list[i]
        count_list[item_list[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, list_size):
        item_list[i] = output_list[i]


data = [4, 2, 2, 4,5,6,3]
count_sort(data)
print("Sorted Array in Ascending Order: ")
print(data)

