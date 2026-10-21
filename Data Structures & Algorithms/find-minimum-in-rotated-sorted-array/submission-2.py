class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        first_elem = nums[0]
        while lower < upper:            
            mid_idx = (lower + upper) // 2
            if nums[mid_idx] >= first_elem:
                lower = mid_idx + 1
            else:
                upper = mid_idx

        return min(first_elem, nums[lower])