class Solution(object):
    def isValid(self, parenthesis):
        """
        :type s: str
        :rtype: bool
        """
        recentOpen=[]
        #recentClosed=[]
        for i in parenthesis:
            if i in ["(","[","{"]:
                recentOpen.append(i)
            elif i in [")","}","]"]:
                #j=recentOpen.pop()
                if len(recentOpen)==0:
                    return False
                j=recentOpen.pop()
                '''try:
                    j=recentOpen.pop()
                except IndexError:
                    #print(f"Invalid Input {i}")
                    return False
                    '''
                if j=="[" and i=="]":
                    pass
                elif j=="{" and i=="}":
                    pass
                elif j=="(" and i==")":
                    pass
                
                else:
                    
                    #print(f"Invalid Input1 {i}")
                    return False
                
            else:
                #print(f"Invalid Input: {i}")
                return False
        
        if len(recentOpen)==0:
            #print("Valid Input")
            return True
        else:
            #print("Invalid Input")
            return False