class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:

        total = m + n

        gap = (total + 1) // 2

        while gap > 0:

            left = 0
            right = left + gap

            while right < total:

                # Both elements are in nums1
                if left < m and right < m:

                    if nums1[left] > nums1[right]:
                        nums1[left], nums1[right] = \
                            nums1[right], nums1[left]

                # left in nums1, right in nums2
                elif left < m and right >= m:

                    if nums1[left] > nums2[right - m]:
                        nums1[left], nums2[right - m] = \
                            nums2[right - m], nums1[left]

                # Both elements are in nums2
                else:

                    if nums2[left - m] > nums2[right - m]:
                        nums2[left - m], nums2[right - m] = \
                            nums2[right - m], nums2[left - m]

                left += 1
                right += 1

            if gap == 1:
                break

            gap = (gap + 1) // 2

        # Copy nums2 into the empty part of nums1
        for i in range(n):
            nums1[m + i] = nums2[i]