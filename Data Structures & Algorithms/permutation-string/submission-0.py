
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        if len(s1) > len(s2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for char in s1:
            freq1[ord(char) - ord('a')] += 1
        for char in s2[:len(s1)]:
            freq2[ord(char) - ord('a')] += 1

        while True:
            if freq1 == freq2:
                return True
            freq2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                freq2[ord(s2[r]) - ord('a')] += 1
            else:
                return False
        return False
