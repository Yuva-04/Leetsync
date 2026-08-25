class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n=len(position)

        def can_we_place(position,dist,balls):
            count_balls=1
            last=position[0]
            for i in range(1,n):
                if position[i]-last >= dist:
                    count_balls += 1
                    last = position[i]

            if count_balls>=balls:
                return True
            else:
                return False

        low = 0
        high = position[n-1]-position[0]
        while low<=high:
            mid = (low+high)//2
            if can_we_place(position,mid,m):
                low=mid+1
            else:
                high = mid -1

        return high
        