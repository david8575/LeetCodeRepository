class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stk = []

        for a in asteroids:
            while stk and stk[-1] > 0 and a < 0:
                if stk[-1] < abs(a):
                    stk.pop()
                    continue
                elif stk[-1] == abs(a):
                    stk.pop()
                    break
                else:
                    break

            else:
                stk.append(a)

        return stk