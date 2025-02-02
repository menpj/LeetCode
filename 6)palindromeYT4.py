#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150
#https://www.youtube.com/watch?v=UPdSViixmDs

class Solution(object):
    def palindrome(self,num) -> bool:
        
        if num == 0:
            print(f"{num} is a Palindrome")
            return True
        elif num<0 or num%10==0:
            print(f"{num} is not a Palindrome")
            return False
        temp=num
        reversed=0
        #length= len(str(temp))
        
        while temp>reversed:
            reversed=(reversed*10)+(temp%10)
            temp=temp//10
            
        if temp==reversed or temp==reversed//10:
            print(f"{num} is a Palindrome")
        else:
            print(f"{num} is not a Palindrome")
    
    
def main():
    solution = Solution()
    num= int(input("Enter a Number:"))
    solution.palindrome(num)
    
main()