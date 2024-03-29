'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        flag = True
        odd = True
        even = True
        ans = ans2 =l1 = l2 = None
        while head!= None:
            if odd or even:
                if odd and flag:
                    ans = l1 = head
                    odd = False
                    flag = False
                else:#if even and not flag:
                    ans2 = l2 = head 
                    even = False
                    flag = True
            else:
                if flag:
                    l1.next = head
                    l1 = l1.next
                    flag = False
                else:
                    l2.next = head
                    l2 = l2.next
                    flag = True   
            head = head.next

        l1.next = ans2
        if l2 != None:
            l2.next = None
        return ans