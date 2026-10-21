class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower <= upper:
            mid = (lower + upper) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            
            if hours > h:
                lower = mid + 1
            elif hours <= h:
                upper = mid - 1

        return lower
