#YT VIDEO INSPITRED SOLUTION,CHECK COMMENT WITH PYTHON CODE
#https://www.youtube.com/watch?v=UcoN6UjAI64

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=0
        for i in range(32):
            bit=n&1
            res=(res<<1)|bit
            n=n>>1
            
        
        return res
        