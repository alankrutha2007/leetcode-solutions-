class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(1,len(points)):
            x1,y1=points[i-1]
            x2,y2=points[i]
            x=abs(x2-x1)
            y=abs(y2-y1)
            time+=max(x,y)
        return time
