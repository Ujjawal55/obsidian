```python
class Solution:

    def transpose(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    def flip(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for j in range(n):
            row = n - 1
            i = 0
            while (i <= row):
                matrix[i][j] , matrix[row][j] = matrix[row][j], matrix[i][j]
                i += 1
                row -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for _ in range(3):
        #     self.transpose(matrix)
        #     self.flip(matrix)


        # OPTIMIZED CODE
        self.transpose(matrix)
        for i in range(len(matrix)):
            matrix[i].reverse()
```
