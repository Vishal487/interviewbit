class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None

    
    def reverseListUtil(self, prev, curr):
        if curr is None:
            return prev
        nxt = curr.next
        curr.next = prev
        return self.reverseListUtil(curr, nxt)

    
    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        curr = head
        prev = None
        return self.reverseListUtil(prev, curr)
        # we can set self.head = returned_value
        # self.head = self.reverseListUtil(prev, curr)



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

    h = ll.reverseList(ll.head)

    ll.printList(h)
