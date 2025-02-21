#not ideal solution,best so far
#working in leetcode

class Solution(object):
    def merge(self,array):
        array3=array[0]
        array=array[1]
        size=len(array)
        if size==1:
            array=[array3,array]
            return array
        
        else:
            
            array1=self.merge([array3[:size//2],array[:size//2]])
            array2=self.merge([array3[size//2:],array[size//2:]])
           
            size1=len(array1[0])
            size2=len(array2[0])
            i,j=0,0
            array=[[],[]]
            while i<size1 and j<size2:
                if array1[1][i]>array2[1][j]:
                    array[1].append(array2[1][j])
                    array[0].append(array2[0][j])
                    j+=1
                    
                else:
                    array[1].append(array1[1][i])
                    array[0].append(array1[0][i])
                    i+=1
                    
                
            while i<size1:
                array[1].append(array1[1][i])
                array[0].append(array1[0][i])
                i+=1
            
                
            while j<size2:
                array[1].append(array2[1][j])
                array[0].append(array2[0][j])
                j+=1
                
            
            return array
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        
        
        maplist=[]
        for i in strs:
           
            

            maplist.append(''.join(sorted(i)))
       
        tobesorted=[strs,maplist]
       
        merged=self.merge(tobesorted)
       
        


        grouplist=[]
        subgroup=[]
        curr=None
        sizemerged=len(merged[1])
        j=0
        while j<sizemerged:
        
            
            if curr==merged[1][j]:
                subgroup.append(merged[0][j])
                
            else:
                if subgroup:
                    
                    grouplist.append(subgroup)   
                subgroup=[]
                
                subgroup.append(merged[0][j])
            
            curr=merged[1][j]
            j+=1
        if subgroup:
            grouplist.append(subgroup)
            
       
        return grouplist

        
         
        