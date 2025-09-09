# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先頭からslowとfastが出会った箇所の距離をk、循環の開始地点からslowとfastが出会った箇所の距離をlとすると
        # 先頭から循環の開始地点までの距離 = slowとfastが出会った箇所から循環の開始地点での距離 = k-l
        # slowをheadに戻して、slowとfastを一つづつ動かしていけば循環の開始地点でslowとfastが出会う
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # headにもどす
        slow = head
        while slow and fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
        return None
