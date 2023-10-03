class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = filter(str.isalnum, s)
        t = "".join(f).casefold()
        inverse = t[::-1]
        return True if t == inverse else False