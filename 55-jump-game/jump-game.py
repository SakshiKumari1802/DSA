class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0  # The farthest index we can currently reach

        # Traverse the array
        for i in range(len(nums)):
            if i > max_index:
                return False  # Cannot proceed further

            # Update farthest reachable index
            max_index = max(max_index, i + nums[i])

        # If loop completes, we can reach the last index
        return True
        