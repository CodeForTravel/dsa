

def binary_search(data_list, data_length, key):
    high = data_length-1
    low = 0

    while(low <= high):
        mid = round((high + low)/2)

        if key == data_list[mid]:
            return mid
        if key < data_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


data_list = [1, 3, 4, 6, 12, 14, 15, 17, 23, 24, 25, 34, 36, 46, 57, 658]
print(binary_search(data_list, len(data_list), 6))
print(binary_search(data_list, len(data_list), 900))
print(binary_search(data_list, len(data_list), 23))
