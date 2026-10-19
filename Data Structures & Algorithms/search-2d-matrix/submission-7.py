class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(row) -> bool:
            left, right = 0, len(row)-1

            while right >= left:
                mid = (right + left) // 2
                curr = row[mid]
                if curr == target:
                    return True
                elif target > curr:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        

        top, bottom = 0, len(matrix) - 1
        while bottom >= top:
            mid_row = (top + bottom) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                return bin_search(matrix[mid_row])
        return False
