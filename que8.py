# You are given an square 2D matrix representing an image, rotate the image by 90 degrees
# (clockwise).
# You have to rotate the image in place, which means you have to modify the input 2D matrix
# directly. DO NOT allocate another 2D matrix and do the rotation.

# Not - in place
'''

mat = [[1,2,3],[4,5,6],[7,8,9]]
n = len(mat)
def rotate_90(mat):
    mat2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat2[j][n-1-i] = mat[i][j]
    return mat2

print(rotate_90(mat))

'''

# In - PLace

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

def inplace_90(mat):
    # Step 1: Transpose the matrix (swap mat[i][j] with mat[j][i])
    for i in range(n):
        for j in range(i + 1, n):  # Ensuring we swap only once
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Step 2: Reverse each row manually
    for i in range(n):
        left, right = 0, n - 1
        while left < right:  # Swap elements from start to end
            mat[i][left], mat[i][right] = mat[i][right], mat[i][left]
            left += 1
            right -= 1

inplace_90(mat)

# Print the rotated matrix
for row in mat:
    print(*row)
