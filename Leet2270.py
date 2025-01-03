#2270. Number of Ways to Split Array

class Solution:
    def waysToSplitArray(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        # Compute prefix sums
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # Compute suffix sums
        total_sum = prefix_sum[-1]

        # Count valid splits
        valid_splits = 0
        for i in range(n - 1):  # Ensure there's at least one element on the right
            left_sum = prefix_sum[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_splits += 1

        return valid_splits

# Example usage
nums1 = [10, 4, -8, 7]
nums2 = [2, 3, 1, 0]

solution = Solution()
print(solution.waysToSplitArray(nums1))  # Output: 2
print(solution.waysToSplitArray(nums2))  # Output: 2
