class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        max_len = 1
        hs = set(s[0])
        while r < len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            curr = r - l + 1
            max_len = max(max_len, curr)
            r += 1
        return max_len
