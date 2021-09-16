class CustomNumber:
    def __init__(self, num):
        self.num = num
    def __lt__(self, other):
        return self.num + other.num < other.num + self.num

class Solution:
    def largestNumber(self, nums) -> str:
        num_str = [CustomNumber(str(num)) for num in nums]
        num_str.sort(reverse=True)
        res = [number.num for number in num_str]
        return str(int("".join(res)))