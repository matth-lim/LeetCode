class Solution:
    def nearestValidPoint(self, x, y, points):
        """
        type x: int
        type y: int
        type points: List[List[int]]
        rtype: int
        """
        dis = 10000
        res = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                distance = abs(x - points[i][0]) + abs(y - points[i][1])
                if distance < dis:
                    dis = distance
                    res = i
        return res