class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = -999
        #counter=len(nums)
        replacedCount=0
        duplicateCount=0
        #listND=[]
        #print(f"First Iteration: \nval: {val}")
        for i in range(len(nums)):
            if nums[i]==val:
                
                duplicateCount+=1
            else:
                #listND.append(nums[i])
                if duplicateCount>=1:
                    nums[replacedCount]=val
                    replacedCount+=1
                    duplicateCount=0
                val=nums[i]
                nums[replacedCount]=val
                replacedCount+=1
        if duplicateCount>=1:
            nums[replacedCount]=val
            replacedCount+=1
            #duplicateCount=0       
        #print(f"list: {list}")
        #len_listND=len(listND)
        #for i in range(len_listND):
        #    nums[i]=listND[i]
                
        #print(nums)
        #print(f"counter: {replacedCount}")
        return replacedCount