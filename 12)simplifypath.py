#71. Simplify Path



class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack=[]
        #re.sub
        s=""
        for i in path:
            if i=='/' and s:
                path_stack.append(s)
                s=""
            elif i=='/':
                pass
    
            else:
                s=s+i
        if s:
            path_stack.append(s)
        #print(path_stack)
        pop_count=0
        #count=0
        for i in range(len(path_stack)):
            if path_stack[i-pop_count]=='.':
                #print("deleeted")
                del(path_stack[i-pop_count])
                pop_count+=1  
            elif path_stack[i-pop_count]=='..':
                #print("enetered")
                
                if ((i-pop_count)%len(path_stack))==0:
                    del(path_stack[i-pop_count])
                    pop_count+=1
                    #print("enetered shit")
                else:
                    #print("enetered didn;t enetr shit")
                    del(path_stack[i-pop_count])
                    pop_count+=1
                    del(path_stack[i-pop_count])
                    pop_count+=1
                
                    
        #print(path_stack)
        
        s=""
        for i in path_stack:
            if i:
                s=s+"/"+i
            
        if not s:
            s="/"
        #print(s)
        return s
                
                
                
                
        
        
def main():
    solution = Solution()
    path=input("Enter the string path: ")
    solution.simplifyPath(path)

main()