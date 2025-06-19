class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n=int(bin(n)[2:])
        print(n)
        multiple=1
        c=""
        count=0
        while n>0:
            c+=str(n%10)
            n=n//10
            count+=1
        while count<32:
            c+="0"
            count+=1
        
        
        return int(c,2)
        