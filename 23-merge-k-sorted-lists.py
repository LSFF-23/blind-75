def toLL (array):
    if len(array) == 0:
        return None
    
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        next = ListNode(array[i])
        current.next = next
        current = next
    return head

def toList (LL):
    result = []
    current = LL
    while current != None:
        result.append(current.val)
        current = current.next
    return result

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from heapq import heappush, heappop

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) == 0:
            return None

        heap = []
        
        for i in range(len(lists)):
            current = lists[i]
            while current != None:
                heappush(heap, current.val)
                current = current.next

        if len(heap) == 0:
            return None
        
        head = ListNode(heappop(heap))
        current = head
        while len(heap) > 0:
            current.next = ListNode(heappop(heap))
            current = current.next

        return head
        

s = Solution()
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
assert toList(s.mergeKLists([toLL([1,4,5]), toLL([1,3,4]), toLL([2,6])])) == [1,1,2,3,4,4,5,6], "#1"
# Input: lists = []
# Output: []
assert toList(s.mergeKLists([])) == [], "#2"
# Input: lists = [[]]
# Output: []
assert toList(s.mergeKLists([toLL([])])) == [], "#3"
assert toList(s.mergeKLists([toLL([1,4,5]), toLL([1,3,4]), toLL([2,6]), toLL([])])) == [1,1,2,3,4,4,5,6], "#4"
# [[],[1]]
assert toList(s.mergeKLists([toLL([]), toLL([1])])) == [1], "#5"