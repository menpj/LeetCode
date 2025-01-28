class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        j=0
        i=0
        
        while i<m or j<n:
            
            if i<m and j<n:
                if nums1[i] > nums2[j]:
                    temp=nums1[i]
                    nums1[i]=nums2[j]
                    if(n-1==0):
                        nums2[j]=temp
                    for k in range(j,n-1):
                        if nums2[k+1]>=temp:
                            
                            nums2[k]=temp
                            break
                        else:
                            if nums2[k+1]<temp:
                                nums2[k]=nums2[k+1]
                                nums2[k+1]=temp
                                
                            
                    i+=1
                   
                else:
                    i+=1
            elif i>=m and j<n and i<m+n:
               
                nums1[i]=nums2[j]
                
                j+=1
                i+=1
    
            elif i<m and j>=n:
               #print("this is executed") 
               break
    
            

                        
                