
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        need, window = [0] * 26, [0] * 26
        for i in range(n):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        for r in range(n, len(s2)):
            if need == window:
                return True
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[r - n]) - ord('a')] -= 1
        return need == window