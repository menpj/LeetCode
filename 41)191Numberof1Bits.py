class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)[2:]
        count=0
        for i in n:
            if i=="1":
                count+=1
        #print(count)
        return count
        #n=int(n,2)
        #print(n)
        