# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.
array = [1, 1, 0, -1, -1]


def plusMinus(arr):
    length = len(arr)
    pos_ints = 0
    neg_ints = 0
    zeros = 0
    for index in range(len(arr)):
        if arr[index] > 0:
            pos_ints += 1
        elif arr[index] == 0:
            zeros += 1
        else:
            neg_ints += 1
    pos_ratio = pos_ints/length
    pos_ratio = format(pos_ratio, ".6f")
    print(pos_ratio)

    neg_ratio = neg_ints/length
    neg_ratio = format(neg_ratio, ".6f")
    print(neg_ratio)

    zero_ratio = zeros/length
    zero_ratio = format(zero_ratio, ".6f")
    print(zero_ratio)


plusMinus(array)
