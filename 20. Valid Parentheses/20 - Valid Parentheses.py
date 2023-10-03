class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in pairs:
                if len(mystack) == 0:
                    return False
                if mystack[-1] == pairs[c]:
                    mystack.pop()
                else:
                    return False
            else:
                mystack.append(c)
        if len(mystack) == 0:
            return True