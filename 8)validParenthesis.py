#20. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

#66. Plus One
#https://www.youtube.com/watch?v=iBk_JyxxuN8
#https://leetcode.com/problems/plus-one/
#this is an ideal solution based on youtube, way better than mine, less complex
class Solution(object):
    def validParentheses(self,parenthesis):
        #pass    
        #return None
        recentOpen=[]
        #recentClosed=[]
        for i in parenthesis:
            if i in ["(","[","{"]:
                recentOpen.append(i)
            elif i in [")","}","]"]:
                if len(recentOpen)==0:
                    return False
                j=recentOpen.pop()
                '''
                try:
                    j=recentOpen.pop()
                except IndexError:
                    print(f"Invalid Input {i}")
                    return False
                '''
                if j=="[" and i=="]":
                    pass
                elif j=="{" and i=="}":
                    pass
                elif j=="(" and i==")":
                    pass
                
                else:
                    
                    print(f"Invalid Input {i}")
                    return False
                
            else:
                print(f"Invalid Input: {i}")
                return False
        
        if len(recentOpen)==0:
            print("Valid Input")
            return True
        else:
            print("Invalid Input")
            return False
    
def main():
    solution = Solution()
    parentheses = input("Enter the brackets: ")
    
    #print(parentheses[0])     
    solution.validParentheses(parentheses)   
        
main()
