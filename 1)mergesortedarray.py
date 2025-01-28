#https://leetcode.com/problems/merge-sorted-array/
#88. Merge Sorted Array
print("hello")
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
j=0
i=0
index=0
print("beginning:")
print(nums1)
print(nums2)
while i<m or j<n:
    print(f"hello1 i:{i} j:{j}")
    if i<m and j<n:
        if nums1[i] > nums2[j]:
            temp=nums1[i]
            nums1[i]=nums2[j]
            if(n-1==0):
                nums2[j]=temp
            for k in range(j,n-1):
                if nums2[k+1]>=temp:
                    print("nums2 element replaced")
                    nums2[k]=temp
                    break
                else:
                    if nums2[k+1]<temp:
                        nums2[k]=nums2[k+1]
                        nums2[k+1]=temp
            
                    
            i+=1
            index+=1
            print(nums1)
            print(nums2)
        else:
            i+=1
    elif i>=m and j<n and i<m+n:
        #temp=nums1[i]
        nums1[i]=nums2[j]
        #nums2[j]=temp
        j+=1
        i+=1
        index+=1
        print(nums1)
        print(nums2)
    elif i<m and j>=n:
        print("execute this")
        print(f"hello2 i:{i} j:{j}")
        break
print(f"answer {nums1}")
print(nums2)

    

                
        