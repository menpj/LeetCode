#67. Add Binary
#https://leetcode.com/problems/add-binary/
#optimal solution
#https://www.youtube.com/watch?v=M9foA9gcL98

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        withC=int(b,2) if a>b else int(a,2)
        withoutC=int(a,2) if a>b else int(b,2)
        while withC:
            temp=withC^withoutC
            withC=(withC & withoutC)<<1
            withoutC=temp
        return bin(withoutC)[2:]