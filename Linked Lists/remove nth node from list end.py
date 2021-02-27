class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        # find length
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next

        if n >= l:  # remove 1st
            head = head.next
            return head

        fromstart = l - n
        temp = head
        cnt = 1
        while cnt < fromstart:
            cnt += 1
            temp = temp.next
        # print(temp.val)
        temp.next  = temp.next.next

        return head



    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [1,2,3,4,5]
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    ll.head.next.next.next.next = Node(myList[4])
    
    ll.printList(ll.head)

    nhead = ll.removeNthFromEnd(ll.head, 4)

    ll.printList(nhead)
