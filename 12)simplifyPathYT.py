#71. Simplify Path
#https://www.youtube.com/watch?v=qYlHrAKJfyA

#not ideal solution



class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack=[]
        #re.sub
        cur=""
        for i in path+'/':
            if i=='/':
                
                if cur=='..':
                    if path_stack:
                    #print("popped")
                        path_stack.pop()
                elif cur!='' and cur!=".":
                    path_stack.append(cur)
                    
                cur=""
        
            else:
                cur=cur+i
        
        #print(path_stack)
        
                
                    
        #print(path_stack)
        #print("/"+"/".join(path_stack))
        
        return "/"+"/".join(path_stack)
        
       
                
                
                
        
        
def main():
    solution = Solution()
    path=input("Enter the string path: ")
    solution.simplifyPath(path)

main()