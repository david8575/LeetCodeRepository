class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)

        idx = 0

        for i in range(m):

            if idx == n:
                return True

            if t[i] == s[idx]:
                idx += 1

        return idx == n