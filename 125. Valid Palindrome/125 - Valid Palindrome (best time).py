class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = filter(str.isalnum, s)
        t = "".join(f).casefold()
        for i in range(int(-(-len(t)/2 // 1))):
            if(t[i] != t[-1*(i+1)]):
                return False
        return True