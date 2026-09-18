class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = []
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else: 
                sum.append(cnt)
                cnt = 0

        sum.append(cnt)

        if len(sum) == 1:
            return sum[0] - 1

        max_len = 0 
        
        for i in range(len(sum)-1):
            max_len = max(max_len, sum[i] + sum[i+1])

        return max_len