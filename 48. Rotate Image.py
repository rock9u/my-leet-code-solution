class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import math
        length = len(matrix)
        timeOfLoop = length//2
        for i in range(timeOfLoop):
            for j in range(i,length-i-1,1):
                self.fourWaySwitch(i,j,matrix,length-1)
        return matrix

    def fourWaySwitch(self,i,j,matrix,length):
        temp = matrix[i][j]
        matrix[i][j] = matrix[length-j][i]
        matrix[length-j][i] = matrix[length-i][length-j]
        matrix[length-i][length-j] = matrix[j][length-i]
        matrix[j][length-i] = temp