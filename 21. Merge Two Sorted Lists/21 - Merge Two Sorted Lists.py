# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rlist = raux = ListNode()

        while True:
            if list1 == None and list2 == None:
                break
            elif list1 == None:
                raux.next = list2
                break
            elif list2 == None:
                raux.next = list1
                break
            elif list1.val < list2.val:
                raux.next = list1
                list1 = list1.next
            else:
                raux.next = list2
                list2 = list2.next
            raux = raux.next
        return rlist.next

                


