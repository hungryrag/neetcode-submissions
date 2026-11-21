class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = [0] * 26
        for i in s:
            a[ord(i)-ord('a')] += 1
        for j in t:
            a[ord(j)-ord('a')] -= 1

        for k in a:
            if k != 0:
                return False
        return True
        