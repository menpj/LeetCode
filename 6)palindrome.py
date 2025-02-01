#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def palindrome(self,num):
        temp=num
        reverseNum=0
        if temp==0:
            print(f"{temp} is Palindrome")
            return True
        while temp>0:
            reverseNum = (reverseNum*10)+(temp%10)
            temp=int(temp/10)
            print(f"After each iteration reverseNum: {reverseNum} temp: {temp}")
        if num==reverseNum:
            print(f"{reverseNum} is Palindrome")
            return True
            
        print(f"{num} is not Palindrome")
        return False
    
    
def main():
    solution = Solution()
    num= int(input("Enter a Number:"))
    solution.palindrome(num)
    
main()