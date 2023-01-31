# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        res = result
        carry = 0
        while l1 or l2:
            summ = 0
            if l1:
                summ += l1.val
            if l2:
                summ += l2.val
            if carry:
                summ += carry
                carry = 0
            if summ >= 10:
                summ = summ % 10
                carry = 1
            res.val = summ
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2:
                res.next = ListNode(0)
                res = res.next
        if carry == 1:
            res.next = ListNode(carry)
            res = res.next
        return result