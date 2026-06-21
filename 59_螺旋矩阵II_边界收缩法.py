# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，
# 且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
from typing import List
# 解题技巧：边界收缩法

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for i in range(n)]
        top,bottom = 0,n-1
        left,right = 0,n-1
        count = 1
        while count <= n**2:
            for j in range(left,right+1):
                mat[top][j] = count
                count += 1
            top += 1
            for i in range(top,bottom+1):
                mat[i][right] = count
                count += 1
            right -= 1
            for j in range(right,left-1,-1):
                mat[bottom][j] = count
                count += 1
            bottom -= 1
            for i in range(bottom,top-1,-1):
                mat[i][left] = count
                count += 1
            left += 1
        return mat

