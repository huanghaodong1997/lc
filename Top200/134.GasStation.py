class Solution:
    # The answer is unique
    def canCompleteCircuit(self, gas, cost) -> int:
        #It's impossible to perform the road trip if sum(gas) < sum(cost). In this situation the answer is -1.
        candidate = 0
        fuel = 0
        total_fuel = 0
        n = len(gas)
        for i in range(n):
            g, c = gas[i], cost[i]
            fuel += g - c
            total_fuel += g -c
            
            #The second fact could be generalized. Let's introduce fuel variable to track the current amount of gas in the tank. If at some station curr_fuel is less than 0, that means that one couldn't reach this station. We must reset the candidate of starting station,
# And we know that the station between last candidate and i will not satisfied because they
# will not lead to a higher curr_fuel, so we just set new candidate it to i + 1

#Next step is to mark this station as a new starting point, and reset curr_fuel to zero since one starts with no gas in the tank.
            if fuel < 0:
                candidate = i + 1
                fuel = 0
        
        #return -1 if total_fuel < 0
        return candidate if total_fuel >= 0 else -1
            