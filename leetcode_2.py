#coding=utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        curr = res
        p = l1
        q = l2
        carry = 0           #初始进位1或0
        
        while p!=None or q!=None:
            x = p.val if p!=None else 0
            y = q.val if q!=None else 0
            sum = carry + x + y
            carry = sum//10              #取整
            curr.next = ListNode(sum%10)
            curr = curr.next

            if p!=None:
                p = p.next
            if q!=None:
                q=q.next
        
        if carry>0:
            curr.next = ListNode(1)

        return res.next


a=ListNode(2)
a.next=ListNode(4)
a.next.next=ListNode(3)
b=ListNode(5)
b.next=ListNode(6)
b.next.next=ListNode(4)

c=Solution()
d=c.addTwoNumbers(a,b)

while d!=None:
    print(d.val)
    d=d.next
