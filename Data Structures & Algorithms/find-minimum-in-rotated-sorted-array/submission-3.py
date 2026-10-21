class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] > nums[upper]:
                lower = mid + 1
            else:
                upper = mid
        return nums[lower]