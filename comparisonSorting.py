array = [1, 3, 54, 76, 32, 1, 6, 8, 5, 4]


def countingSort(arr):
    frequency_array = [0]*100
    print(frequency_array)
    for i in range(100):
        frequency_array[i] = arr.count(i)
    return frequency_array


countingSort(array)
