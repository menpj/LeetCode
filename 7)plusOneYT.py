#66. Plus One
#https://www.youtube.com/watch?v=iBk_JyxxuN8
#https://leetcode.com/problems/plus-one/
#this is an ideal solution based on youtube, way better than mine, less complex
class Solution(object):
    def plusOne(self,digits):
        length=len(digits)
         
    
        '''if digits[length-1]!=9:
            digits[length-1]+=1
            print(digits)
            return digits
        
        else:'''
        for i in range(length-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            
            digits[i]=0
            
        digits=[0 for _ in range(length+1)]
        digits[0]=1
        
        print(digits)
        return digits 
                
                    

                
                 
    
    
def main():
    solution = Solution()
    arrayElement = []
    print("Enter elements one by one, enter 'stop' when it is finished")
    
    while True:
        num=input("Enter digit:")
        if num.lower()=="stop":
            break
        try:
            num=int(num)
            if 0<=num and 9>=num: 
                arrayElement.append(num)
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid digit between 0 to 9")
    print(arrayElement)     
    solution.plusOne(arrayElement)   
        
main()
