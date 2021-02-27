class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None

    
    def kthNodeFromMiddle(self, head, k): 
        l = 0 
        temp = head
        while temp:
            l += 1
            temp = temp.next
        mid = (l//2) + 1  
        cnt = 1
        temp = head
        pos = mid - k
        if pos <= 0:
            return -1
        while cnt < pos:    
            cnt += 1
            temp = temp.next
        return temp.val



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

    n = ll.kthNodeFromMiddle(ll.head, 2)

    print(n)
