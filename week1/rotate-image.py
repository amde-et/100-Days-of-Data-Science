class Solution:
    def rotate(self, matrix):
        matrix.reverse()
      
        for i in range(len(matrix)):
            for j in range(i):
                
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
