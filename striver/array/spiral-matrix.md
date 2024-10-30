#### Idea is to just try to write a code and then modify it to change the base cases.

> ##### NOTE: Most important notes is that try to be consistent with the symbol that you choose in the program and don't mix them.

(https://leetcode.com/problems/spiral-matrix)

```python

class Solution:

    def spiralList(self, matrix, i, j, n, m,  lst) -> list:

    # store the coordinate of all the four corners
        tl = [i, j]
        tr = [i, m - j]
        br = [n-i, m - j]
        bl = [n - i, j]

        print(f"tl: {tl}, tr: {tr}, br: {br}, bl: {bl}")

        # base case

        # square matrix with even size
        if tl[1] > tr[1] or bl[1] > br[1] or tl[0] > bl[0] or tr[0] > br[0]:
            return lst

        # square matrix with odd size.
        if tl == tr == bl == br:
            lst.append(matrix[tl[0]][tl[1]])
            return lst

        # vertical matrix
        if tl == tr and bl == br:
            for k in range(tl[0], bl[0] + 1):
                lst.append(matrix[k][tl[1]])
            return lst

        # horizontal matrix

        if tl == bl and tr == br:
            for k in range(tl[1], tr[1] + 1):
                lst.append(matrix[tl[0]][k])
            return lst

        # spinal case....

        # left -> right with both end inclusive
        for k in range(tl[1] , tr[1] + 1):
            lst.append(matrix[tl[0]][k])

        # top to bottom with both end exclusive
        if n - 2 * i > 1:
            for k in range(tr[0] + 1, br[0]):
                lst.append(matrix[k][tr[1]])

        # right to left with both end inclusive
        for k in reversed(range(bl[1], br[1] + 1)):
            lst.append(matrix[br[0]][k])

        # bottom to up
        if n - 2 * i > 1:
            for k in reversed(range(tl[0] + 1, bl[0])):
                lst.append(matrix[k][tl[1]])

        return self.spiralList(matrix, i + 1, j + 1, n, m, lst)


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiralList(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1,  [])
```

![[spiral-matrix.pdf]]
