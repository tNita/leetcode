# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        rnode = None
        while True:
            if node == None:
                break
            rnode = ListNode(node.val, rnode)
            node = node.next
        return rnode
        # if head is None or head.next is None:
        #     return head

        # # 残りの部分を反転
        # new_head = self.reverseList(head.next)

        # # ポインタの付け替え
        # head.next.next = head
        # head.next = None

        # return new_head
