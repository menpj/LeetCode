#20. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150
#https://www.youtube.com/watch?v=WTzjTskDFMg YouTube solution.
#this is an ideal solution


class Solution(object):
    def isValid(self, parenthesis):
        """
        :type s: str
        :rtype: bool
        """
        closetoopen = {')':'(',']':'[','}':'{' }
        recentOpen=[]
        #recentClosed=[]
        for i in parenthesis:
            if i in closetoopen:
                if recentOpen and recentOpen[-1]==closetoopen[i]:
                    recentOpen.pop()
                else:
                    #print(f"Invalid Input {i}")
                    return False
            else:
                recentOpen.append(i)
        return True if not recentOpen else False
    