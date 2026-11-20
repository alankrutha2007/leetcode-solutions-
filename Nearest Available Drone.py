class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        min_dist = float('inf')
        ans = -1
        for i in range(len(drones)):
            x = drones[i][0]
            y = drones[i][1]
            r = drones[i][2]
            dist = abs(x - target[0]) + abs(y - target[1])
            if dist <= r:
                if dist < min_dist:
                    min_dist = dist
                    ans = i
        return ans
