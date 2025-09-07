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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        if list1 != None and list2 == None:
            return list1
        if list1 == None and list2 != None:
            return list2
        
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next

        current = head
        while current != None:
            if list1 == None:
                current.next = list2
                break
            if list2 == None:
                current.next = list1
                break
            
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next

            current = current.next

        return head

s = Solution()
assert toList(s.mergeTwoLists(toLL([1,2,4]), toLL([1,3,4]))) == [1,1,2,3,4,4], "#1"
assert toList(s.mergeTwoLists(toLL([]), toLL([]))) == [], "#2"
assert toList(s.mergeTwoLists(toLL([]), toLL([0]))) == [0], "#3"
assert toList(s.mergeTwoLists(toLL([1, 1, 2, 3]), toLL([1, 3, 4]))) == [1, 1, 1, 2, 3, 3, 4], "#4"