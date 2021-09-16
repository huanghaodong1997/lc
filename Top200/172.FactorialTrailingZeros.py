class Solution:
    def trailingZeroes(self, n: int) -> int:
        #So, how many times do we multiply by 1010 while calculating n!n!
        # how many 5 in factors
         # we can notice that twos is always bigger than fives. Why? Well, every second number counts for a 22 factor, but only every fifth number counts as a 55 factor. Similarly every 4th number counts as an additional 22 factor, yet only every 25th number counts an additional 55 factor. This goes on and on for each power of 22 and 55
            
        # don;t need to calculate the numbers of factor 5
        
        #Well, by counting the number of multiples of 5 up to n, we're just counting how many 55s go into nn. That's the exact definition of integer division!
        
        zero_count = 0
        current_multiple = 5
        
        # n // current_multiple: how many numbers below m can be divided by current multiple
        while n >= current_multiple:
            # n // 5
            # n // 25 because you have calculate the factor in n // 5, so you only calculate the other factor here
            # n // 125 = n // 5 * 5 * 5, you have calculated the two factors in previous step
            zero_count += n // current_multiple
            current_multiple *= 5
        return zero_count