class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        diff = {}
        for i in range(len(s)):
            if s[i] not in diff:
                diff[s[i]] = 1
            else:
                diff[s[i]] += 1
        print(diff)
        for j in range(len(t)):
            if t[j] not in diff:
                return False
            else:
                diff[t[j]]-=1
                if diff[t[j]] == 0:
                    del diff[t[j]]
        return True
        