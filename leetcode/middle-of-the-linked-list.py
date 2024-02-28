# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1=head
        count=1
        while temp1.next!=None:
            temp1=temp1.next
            count+=1
        
        mid=count//2
        temp1=temp1.next
        temp=head
        for i in range(mid):
            temp=temp.next
        head=temp
        return head
        






