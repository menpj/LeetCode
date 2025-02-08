#704. Binary Search
#https://www.youtube.com/watch?v=s4DPM8ct1pI
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                print(f"Item FOund at  {mid}")
                return mid
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
                
        print("Item not found")
        return -1
                
        
def main():
    a = []
    while True:
        s = input("Enter Elements(s to stop): ")
        if s=='s':
            break
        else:
            a.append(int(s))
    b = int(input("Enter target number: "))
    solution = Solution()
    
    solution.search(a,b)
main()
    
        