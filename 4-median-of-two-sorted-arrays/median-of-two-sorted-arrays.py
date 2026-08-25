class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        n1=len(nums1)
        n2=len(nums2)
        low = 0
        high = n1

        int_min=float('-inf')
        int_max=float('inf')

        while low <=high:
            cut1=(low+high)//2
            cut2=(n1+n2+1)//2 -cut1

            left1=int_min if cut1==0 else nums1[cut1-1]
            left2=int_min if cut2==0 else nums2[cut2-1]

            right1=int_max if cut1==n1 else nums1[cut1]
            right2=int_max if cut2==n2 else nums2[cut2]

            if left1<=right2 and left2<=right1:
                if (n1+n2)%2 == 0:
                    return (max(left1,left2)+min(right1,right2))/2
                else:
                    return max(left1,left2)

            elif left1>right2:
                high=cut1-1
            else:
                low=cut1+1
        
        return 0
              
        