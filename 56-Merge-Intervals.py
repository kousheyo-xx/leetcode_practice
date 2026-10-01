class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged=[]
        merged.append(intervals[0])
        n=len(intervals)
        for i in range(1,n):
            if intervals[i][0]<=merged[-1][1]:
                merged[-1][1]=max(intervals[i][1],merged[-1][1])
            else:
                merged.append(intervals[i])
        return merged