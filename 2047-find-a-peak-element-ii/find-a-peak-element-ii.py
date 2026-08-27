class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def maxIndex(mat, n, m, col):
            max_value = -1
            index = -1

            for i in range(n):
                if mat[i][col] > max_value:
                    max_value = mat[i][col]
                    index = i

            return index

        n = len(mat)
        m = len(mat[0])

        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2

            max_row_index = maxIndex(mat, n, m, mid)

            left = mat[max_row_index][mid - 1] if mid - 1 >= 0 else -1
            right = mat[max_row_index][mid + 1] if mid + 1 < m else -1

            if mat[max_row_index][mid] > left and \
               mat[max_row_index][mid] > right:
                return [max_row_index, mid]

            elif mat[max_row_index][mid] > left:
                low = mid + 1

            else:
                high = mid - 1

        return [-1, -1]