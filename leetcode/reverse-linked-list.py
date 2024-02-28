# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack=[]
        temp=head
        prev=None
        while temp :
            cur=temp.next
            temp.next=prev
            prev=temp  
            temp=cur
        head=prev
        return head
        

            