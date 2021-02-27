class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            tempNext = curr.next 
            curr.next = prev
            prev = curr 
            curr = tempNext

        self.head = prev 
        return self.head  



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

    revHead = ll.reverse(ll.head)

    ll.printList(ll.head)

