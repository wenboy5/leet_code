'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
'''

'''
To find the max product of 8, break up 8 into the sum of two terms (keep the first term less than or equal to the second to prevent redundancy):

1 + 7 --> 1 * 7 = 7
2 + 6 --> 2 * 6 = 12
3 + 5 --> 3 * 5 = 15
4 + 4 --> 4 * 4 = 16
From this is seems that the max product 16, however we neglected to also break up each of the two terms into more terms, and check all those. Let's break the 6 into 3 + 3:

2 + 6 = 2 + 3 + 3 --> 2 * 3 * 3 = 18
which ends up being the correct answer. But another way to get this is to reuse the previously computed max product of 6, which we know to be 9:

2 * (3 * 3) = 2 * max_product_of_6 = 2 * 9 = 18
So for each choice of i and j with i <= j and i + j = n, check i * j but ALSO check if the previously computed max products for i and j are larger than i and j. Start with n = 1 and build up to the final n. Store the previously computed values in a dp list.
''''
class Solution(object):
    def integerBreak(self, n):
        dp = [None, 1]
        for m in range (2, n + 1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)
        return dp[n]
'''
From the hint:

7 = 3 + 4 = 12

8 = 3 + 3 + 2 = 18

9 = 3 + 3 + 3 = 27

10 = 3 + 3 + 4 = 36

11 = 3 + 3 + 3 + 2 = 54

12 = 3 + 3 + 3 + 3 = 81

Three is a magic number.
''''
class Solution(object):
    def integerBreak(self, n):
        if n == 2 or n == 3:
            return n - 1
        if n % 3 == 0:
            return 3**(n/3)
        if n % 3 == 1:
            return 3**(n/3 - 1)*4
        if n % 3 == 2:
            return 3**(n/3)*2