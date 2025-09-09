# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # current = head
        # already = set()
        # while True:
        #     if current is None:
        #         return False
        #     if current in already:
        #         return True
        #     already.add(current)
        #     current = current.next
