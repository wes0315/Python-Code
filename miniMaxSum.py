# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
array = [1, 3, 5, 7, 9]


def miniMaxSum(arr):
    arr = sorted(arr)
    minimum_sum = 0
    maximum_sum = 0
    for index in range(len(arr)-1):
        minimum_sum += arr[index]
    for max_index in range(len(arr)):
        if max_index != 0:
            maximum_sum += arr[max_index]
    print(f"minimum_sum={minimum_sum}, maximum_sum={maximum_sum}")


miniMaxSum(array)
