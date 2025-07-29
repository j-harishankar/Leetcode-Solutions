class Solution(object):
    def diagonalSum(self, mat):
        sum=0 
        k = len(mat)
        for i in range(k):
            sum += mat[i][i]
            sum += mat[i][k-1-i]
        i = k%2
        c = k//2
        if i!=0:
            sum-=mat[c][c]
        return sum