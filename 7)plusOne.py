#66. Plus One
#https://leetcode.com/problems/plus-one/


class Solution(object):
    def plusOne(self,digits):
        length=len(digits)
        carry=1
        '''if digits[length-1]!=9:
            digits[length-1]+=1
            print(digits)
            return digits
        
        else:'''
        for i in range(length-1,-1,-1):
            if carry==0:
                break
            
            elif carry==1 and i!=0:
                if digits[i]==9:
                
                    digits[i]=0
                else: 
                    digits[i]+=1
                    carry=0
            elif carry==1 and i==0:
                if digits[i]!=9:
                    digits[i]+=1
                    carry=0
                else:
                    digits[i]=0
                    for j in range(length-1,-1,-1):
                        if j==length-1:
                            digits.append(digits[j])
                        else:
                            digits[j+1]=digits[j]
                    digits[0]=1
                    carry=0
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