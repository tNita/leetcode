# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dummy_currrent = dummy
        currrent = head

        while currrent:
            # 同じ場合は寄せる
            while currrent.next and currrent.val == currrent.next.val:
                currrent = currrent.next

            # prev.next が cur そのものなら重複なし（この値は1個だけ）
            if dummy_currrent.next is currrent:
                dummy_currrent = dummy_currrent.next
            else:
                # スキップ
                dummy_currrent.next = currrent.next
            currrent = currrent.next
        return dummy.next
