class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0] * 26
        for i in s:
            a[ord(i)-97] += 1
        for j in t:
            a[ord(j)-97] -= 1

        for k in a:
            if k != 0:
                return False
        return True
        