class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        for row in matrix:
            dict1 = {}
            for element in row:
                if element in dict1.values():
                    return False
                else:
                    dict1[element] = element
        for i in range(n):
            dict1 = {}
            for j in range(n):
                if matrix[j][i] in dict1.values():
                    return False
                else:
                    dict1[matrix[j][i]] = matrix[j][i]
        return True
        