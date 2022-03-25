class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        
        
        def timeToCatch(car1, car2):
            pos1, speed1 = car1
            pos2, speed2 = car2
            pos_diff, speed_diff = pos2 - pos1, speed1 - speed2
            if speed_diff <= 0:
                return -1
            return pos_diff / speed_diff
        
        n = len(cars)
        
        res = [-1] * n
        
        stk = []
        
        for i in range(n - 1, -1, -1):
            # 
            car = cars[i]
            # Pop the element when
            # 1. your speed is lower than car on stk[-1]
            # 2. res[stk[-1]] is the time the car on the right side of cars[i] catch its next car, you should pop the element if you can catck the "next car" before you catch cars[stk[-1]]
            while stk and (car[1] <= cars[stk[-1]][1] or timeToCatch(car, cars[stk[-1]]) >= res[stk[-1]] > 0):
                stk.pop()
            if stk:
                res[i] = timeToCatch(cars[i], cars[stk[-1]])
            stk.append(i)
        return res