class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(K):
            left=0
            total=0
            count=0
            for right in range(len(nums)):
                if K < 0:
                    return 0
                total +=nums[right]
                while total > K:
                    total -= nums[left]
                    left +=1
                count += right - left +1
            return count

        return atMost(goal) - atMost(goal-1)
        