## Blog link: https://brain.dennyzhang.com/rectangle-area
## Basic Ideas:
##     width: min(C,G)-max(A,E)
##     height: min(D, H)-max(B,F)
##
##     If width or height is not positive, they won't overlap
##
## Complexity: Time O(1), Space O(1)
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = abs(C-A)*abs(B-D)
        area2 = abs(E-G)*abs(F-H)
        w = min(C,G)-max(A,E)
        h = min(D, H)-max(B,F)
        if w<=0 or h<=0:
            return area1 + area2
        else:
            return area1 + area2 - w*h