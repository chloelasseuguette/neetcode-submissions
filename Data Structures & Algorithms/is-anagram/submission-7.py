class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = False
        if len(s) == len(t):
            characters_s = []
            characters_t = []
            for i in range(len(s)):
                characters_s.append(s[i])
                characters_t.append(t[i])
            characters_s.sort()
            characters_t.sort()
            if characters_s == characters_t:
                flag = True
        return flag

        
                    