class Solution(object):
    def kClosest(self, points, k):
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:k]
        