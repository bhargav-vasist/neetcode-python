class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            charList = [0] * 140
            for i in range(len(s)):
                char1 = s[i]
                char2 = t[i]
                if char1 == char2:
                    continue
                else:
                    charList[ord(char1)] += 1
                    charList[ord(char2)] -= 1
            for val in charList:
                if val != 0:
                    return False
                else:
                    continue
            return True

    def isAnagramPerf(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
