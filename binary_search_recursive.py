

def recursive_binary_search(data_list, l, h, key):
    if l == h:
        if data_list[l] == key:
            return l
        else:
            return -1

    else:
        mid = round((l+h)/2)
        if key == data_list[mid]:
            return mid
        if key < data_list[mid]:
            return recursive_binary_search(data_list, l, mid-1, key)
        else:
            return recursive_binary_search(data_list, l+1, h, key)


data_list = [1, 3, 4, 6, 12, 14, 15, 17, 23, 24, 25, 34, 36, 46, 57, 658]
print(recursive_binary_search(data_list, 0, len(data_list)-1, 6))
print(recursive_binary_search(data_list, 0, len(data_list)-1, 900))
print(recursive_binary_search(data_list, 0, len(data_list)-1, 23))
