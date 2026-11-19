class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while (r-l+1) > k + max(freq.values()):
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len