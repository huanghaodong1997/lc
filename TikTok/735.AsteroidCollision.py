class Solution:
    def asteroidCollision(self, asteroids):
        stk = []
        
        for mass in asteroids:
            boom = False
            while stk and mass < 0 and stk[-1] > 0:
                if stk[-1] < -mass:
                    stk.pop()
                    continue
                elif stk[-1] == -mass:
                    stk.pop()
                    boom = True
                    break
                else:
                    boom = True
                    break
            if not boom:
                stk.append(mass)
        return stk
                
            