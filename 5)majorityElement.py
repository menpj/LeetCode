#169. Majority Element
#https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
#MyOwnSOlution
class Solution(object):
    def majorityElement(self,nums):
    
        counter={}
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        #return max(counter,key=counter.get))
        maxValue=float('-inf')
        maxKey=None
        for key in counter:
            if counter[key]>maxValue:
                maxValue=counter[key]
                maxKey=key
        print(f"maxvalue: {maxValue} maxkey: {maxKey}")
        return maxValue
	
def main():
    solution=Solution()
    solution.majorityElement([3,2,3])

main()