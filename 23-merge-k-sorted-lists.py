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

class Solution(object):
    def mergeKLists(self, lists: list):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) == 0:
            return None

        head = None
        fIndex = -1
        for i in range(len(lists)):
            if lists[i] == None:
                pass
            elif fIndex == -1 or lists[i].val < lists[fIndex].val:
                fIndex = i

        if fIndex == -1: 
            return None
        
        head = lists[fIndex]
        lists[fIndex] = lists[fIndex].next

        current = head
        while current != None:
            kIndex = -1
            for i in range(len(lists)):
                if lists[i] == None:
                    pass
                elif kIndex == -1 or lists[i].val < lists[kIndex].val:
                    kIndex = i
            
            if kIndex == -1:
                break

            current = lists[kIndex]
            lists[kIndex] = lists[kIndex].next

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
assert toList(s.mergeKLists([[]])) == [], "#3"