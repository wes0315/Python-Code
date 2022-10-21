# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]


def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    right_index = len(arr)-1
    for index in range(len(arr)):
        left_diagonal += arr[index][index]
        right_diagonal += arr[index][right_index]
        right_index -= 1
    # print(f"Left Diagonal sum:{left_diagonal}")
    # print(f"Right Diagonal sum:{right_diagonal}")
    return (abs(left_diagonal-right_diagonal))


print(diagonalDifference(arr))
