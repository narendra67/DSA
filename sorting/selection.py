"""Selection sort algo."""


def swap(array, index_one, index_two):
    """Swap to indexes in a given array."""
    temp = array[index_one]
    array[index_one] = array[index_two]
    array[index_two] = temp


def indexOfMinimum(array, start_index):
    """Find the least number from the start_index pos and retur the index."""
    min_index = start_index
    min_value = array[start_index]
    new_array = array[min_index + 1:]
    # print(new_array)

    for index, value in enumerate(new_array):
        # print('in for', index, value, index + start_index + 1)
        if value < min_value:
            # print('in condition', value, min_value)
            min_index = start_index + index + 1
            min_value = value

    return min_index


# arr = [0, 2, -7, -7, 6, 4, -5, 1]
# indexOfMinimum(arr, 0)

def selectionSort(array):
    for index, value in enumerate(array):
        min_index = indexOfMinimum(array, index)
        swap(array, index, min_index)
    
    print(array, sorted(array))
    return array


# array = [4, 7, 99, -10, -23, 15, 6, 0, 73]
# selectionSort(array)
