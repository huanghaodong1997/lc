# follow up: can you do this without convert it to string
# Revert half of the number and compare it to the first half
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if last digit is zero, False
        if x < 0 or x % 10 == 0 and x != 0 : return False
        
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == reverted or x == reverted // 10