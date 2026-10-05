class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:
            if i == "]":
                x = ""

                while stack[-1] != "[":
                    x = stack.pop() + x

                stack.pop()

                times = ""

                while stack and stack[-1].isdigit():
                    times = stack.pop() + times

                stack.append(int(times)*x)

            else:
                stack.append(i)

        return "".join(stack)