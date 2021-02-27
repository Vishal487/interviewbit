class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")



def lengthOfList(head):
    temp = head
    l = 0
    while temp != None:
        l += 1
        temp = temp.next
    return l


def getIntersectionNode(head1, head2):
    l1 = lengthOfList(head1)
    l2 = lengthOfList(head2)
    
    temp1 = head1
    temp2 = head2

    if l1 > l2:
        diff = l1 - l2
        cnt = 0
        while cnt != diff:
            temp1 = temp1.next
            cnt += 1
    elif l1 < l2:
        diff = l2 - l1
        cnt = 0
        while cnt != diff:
            temp2 = temp2.next 
            cnt += 1

    while temp1 and temp2:
        if temp1 == temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next
    return None   



if __name__ == "__main__":
    myList = [1,2,3,4,5]
    myList2 = [10,20,30] 

    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    ll.head.next.next.next.next = Node(myList[4])
    
    ll2 = ListNode()
    ll2.head = Node(myList2[0])
    ll2.head.next = Node(myList2[1])
    ll2.head.next.next = Node(myList2[2])
    ll2.head.next.next.next = ll.head.next.next

    ll.printList(ll.head)
    ll2.printList(ll2.head)

    iNode = getIntersectionNode(ll.head, ll2.head)
    print("intersection node value: ", iNode.val)