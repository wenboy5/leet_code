'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        for i, e in enumerate(s):
            if e not in "()":
                continue
            if e == "(":
                stack.append(i)
            else:
                if stack == []:
                    remove.append(i)
                else:
                    stack.pop()
        remove = set(stack + remove)
        ans = []
        for i, e in enumerate(s):
            if i not in remove:
                ans.append(e)
        return "".join(ans)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s = list(s) # s只有转化为list才能遍历 
        stack = []
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[index] = ''
        for i in stack:
            s[i] = ''
        return ''.join(s)