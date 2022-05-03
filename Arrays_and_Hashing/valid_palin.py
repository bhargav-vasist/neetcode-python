class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitizedStr = "".join(ch for ch in s.lower() if ch.isalnum())
        print(sanitizedStr)
        for idx in range(len(sanitizedStr)):
            revIdx = len(sanitizedStr) - idx - 1
            if idx == revIdx:
                return True
            if sanitizedStr[idx] == sanitizedStr[revIdx]:
                continue
            else:
                print(sanitizedStr[idx], sanitizedStr[revIdx])
                return False
        return True

    def isPalindromeEff(self, s: str) -> bool:
        s = "".join(ch for ch in s.lower() if ch.isalnum())
        return s == s[::-1]


print(Solution().isPalindromeEff("A man, a plan, a canal: Panama"))
