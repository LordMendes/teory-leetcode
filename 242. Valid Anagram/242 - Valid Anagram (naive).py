class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        sDict={}
        tDict={}
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]]+=1
            else:
                sDict[s[i]]=1
            if t[i] in tDict:
                tDict[t[i]]+=1
            else:
                tDict[t[i]]=1

        if(len(sDict)!=len(tDict)):
            return False
        
        for c in sDict:
            if(not c in tDict):
                return False
            if(sDict[c] != tDict[c]):
                return False
        return True