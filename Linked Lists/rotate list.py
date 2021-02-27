class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def rotateList(self, head, k):
        temp = head
        l = 0
        while temp.next:
            l += 1
            temp = temp.next
        l += 1
        if k == 0 or (abs(l-k))%l == 0:
            return head
        temp.next = head

        temp = head
        cnt = 1
        prev = None
        if k > l:
            k = k%l 

        pos = l-k
        while cnt <= pos:
            cnt += 1
            prev = temp
            temp = temp.next
        prev.next = None
        head = temp

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

    nh = ll.rotateList(ll.head, 12)

    ll.printList(nh)
