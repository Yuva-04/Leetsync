class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        xor = 0

        # XOR numbers from 1 to n
        for i in range(1, n + 1):
            xor ^= i

        # XOR all array elements
        for num in nums:
            xor ^= num

        # Find rightmost set bit
        bit = xor & -xor

        x = 0
        y = 0

        # Divide 1...n into two groups
        for i in range(1, n + 1):
            if i & bit:
                x ^= i
            else:
                y ^= i

        # Divide nums into two groups
        for num in nums:
            if num & bit:
                x ^= num
            else:
                y ^= num

        # Determine which is repeating and which is missing
        for num in nums:
            if num == x:
                return [x, y]

        return [y, x]
        