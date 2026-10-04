class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []

        for i in s:
            if i == "*":
                ans.pop()
            else:
                ans.append(i)

        return "".join(ans)