class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def addTwoNumbers(self, head1, head2):
        temp1 = head1
        temp2 = head2

        fst = temp1.val + temp2.val
        carry = 0
        if fst >= 10:
            fst = fst%10
            carry = 1
        head = Node(int(float(fst)))
        temp = head

        temp1 = temp1.next
        temp2 = temp2.next
        while True:
            if temp1 == None and temp2 == None:
                break
            if temp1 and temp2:
                s = temp1.val + temp2.val + carry
                carry = 0
                if s >= 10:
                    s = s%10
                    carry = 1
                temp.next = Node(s)
                temp = temp.next

                temp1 = temp1.next
                temp2 = temp2.next
            if temp1 and not temp2:
                s = temp1.val + carry
                carry = 0
                if s >= 10:
                    s = s%10
                    carry = 1
                temp.next = Node(s)
                temp = temp.next

                temp1 = temp1.next
            if not temp1 and temp2:
                s = temp2.val + carry
                carry = 0
                if s >= 10:
                    s = s%10
                    carry = 1
                temp.next = Node(s)
                temp = temp.next

                temp2 = temp2.next
        if carry == 1:
            temp.next = Node(1)

        return head


    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [1]
    ll = ListNode()
    ll.head = Node(myList[0])
    # ll.head.next = Node(myList[1])
    # ll.head.next.next = Node(myList[2])
    # ll.head.next.next.next = Node(myList[3])
    # ll.head.next.next.next.next = Node(myList[4])

    myList = [9,9,9]
    ll2 = ListNode()
    ll2.head = Node(myList[0])
    ll2.head.next = Node(myList[1])
    ll2.head.next.next = Node(myList[2])
    
    ll.printList(ll.head)
    ll2.printList(ll2.head)

    h = ll.addTwoNumbers(ll.head, ll2.head)

    ll.printList(h)