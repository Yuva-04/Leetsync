class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def sumbyD(nums, div):
            total = 0

            for i in range(len(nums)):
                total += (nums[i] + div - 1) // div

            return total

        low = 1
        high = max(nums)

        while low <= high:

            mid = (low + high) // 2

            if sumbyD(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low