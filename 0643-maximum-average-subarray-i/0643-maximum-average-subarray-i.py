class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k]) 
        window_avg = window_sum / float(k)

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            window_avg = max(window_avg, window_sum / float(k))

        return window_avg