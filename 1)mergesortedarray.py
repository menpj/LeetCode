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
while i<m or j<n:
    print(f"hello1 i:{i} j:{j}")
    if i<m and j<n:
        if nums1[i] > nums2[j]:
            temp=nums1[i]
            nums1[i]=nums2[j]
            nums2[j]=temp
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
print(nums1)
print(nums2)

    

                
        