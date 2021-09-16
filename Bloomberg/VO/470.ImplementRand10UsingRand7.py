def rand7():
    return 0
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            
            if idx <= 40:
                return 1 + (idx - 1) % 10

class UtilizeSolution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            
            # idx range now : (1:49)
            # u need to reject 41 : 49
            if idx <= 40:
                return 1 + (idx - 1) % 10
            
            # idx range now: (1 : 63)
            # u only need to reject 61:63
            row = idx - 40
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 60:
                return 1 + (idx - 1) % 10
            
            # continue with the process
            # idx range now: (1:21)
            # u only need to reject 1
            row = idx - 60
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 20:
                return 1 + (idx - 1) % 10