#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150
#https://www.youtube.com/watch?v=yubRKwixN-U inspired from this video but solution is not ideal

class Solution(object):
    def palindrome(self,num) -> bool:
        
        
        temp=num
        length= len(str(temp))
        i=0
        if num<0:
            print(f"{num} is not a Palindrome")
            return False
        while temp>0 and length>1:
            if temp%10 == int(temp/(10**(length-1))):
                #temp=temp%(10**length-1)
                temp=temp%(10**(length-1))
                temp=int(temp/10)
                
                length-=2
                #print(f"After iteration {temp} length: {length}")
            else:
                #print(f"{num} is not a Palindrome")
                return False
            
        
        
            
        print(f"{num} is a Palindrome")
        return True
    
    
def main():
    solution = Solution()
    num= int(input("Enter a Number:"))
    solution.palindrome(num)
    
main()