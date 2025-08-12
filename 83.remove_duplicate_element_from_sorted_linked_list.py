# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        val = head.val
        nextVal = head.next.val
        if val == nextVal:
            # ポインタ付け替え
            head.next = head.next.next

        (
            self.deleteDuplicates(head)
            if val == nextVal
            else self.deleteDuplicates(head.next)
        )
        return head

        # node = head
        # while True:
        #     if node == None or node.next == None:
        #         break
        #     if node.val == node.next.val:
        #         node.next = node.next.next
        #         continue

        #     node = node.next

        # return head
