class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for i in intervals:
            if i[1] < newInterval[0]:
                res.append(i)
            elif i[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = i
            else:
                newInterval[0] = min(newInterval[0] ,  i[0])
                newInterval[1] = max(newInterval[1] , i[1])
        res.append(newInterval)
        return res
