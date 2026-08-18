class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1

        first = -1
        last = -1

        # Find first occurrence
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        # Reset for second binary search
        low = 0
        high = len(nums) - 1

        # Find last occurrence
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return [first, last]