# given a square matrix, calculate the absolute difference between the sums
# of its diagonals.
# 123
# 456
# 989
# The left-to-right diagonal = 1+5+9 = 15, The right to left diagonal 3+5+9 = =
# 17, Their absolute difference is 115-171 = 2
#

#  1    2   3
#  4    5   6
#  9    8   9

'''
def absolute_difference(arr):
    i = 0
    j = len(arr) - 1
    sum_1 = 0
    sum_2 = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                sum_1 += arr[i][j]
    for i in range(len(arr) - 1, 0, -1):
        for j in range(len(arr)):
            sum_2 += arr[i][j]
            break
    return abs(sum_1 - sum_2)
    
'''
def absolute_difference(arr):
    n = len(arr)
    sum_1 = 0  # Left-to-right diagonal sum
    sum_2 = 0  # Right-to-left diagonal sum

    for i in range(n):
        sum_1 += arr[i][i]          # Main diagonal (i, i)
        sum_2 += arr[i][n - 1 - i]  # Anti-diagonal (i, n-1-i)

    return abs(sum_1 - sum_2)

arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

print(absolute_difference(arr))