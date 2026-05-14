class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
       #0, 2 
       #
        while l < r:
            for i in range(r - l): #2 - 0 
                lu, ru, rd, ld = matrix[l][l + i], matrix[l + i][r], matrix[r][r - i], matrix[r -i][l]
                matrix[l][l + i], matrix[l + i][r], matrix[r][r - i], matrix[r -i][l] = ld, lu, ru, rd
            l , r = l + 1, r - 1

                