class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def swapPairs_pointers(self, head):
        temp = head
        if not temp.next:
            return head

        first = temp
        second = first.next

        head = second
        first.next = second.next
        second.next = first
        prev = first

        while True:
            if first.next:
                first = first.next
                if first.next:
                    second = first.next
                else:
                    break
            else:
                break

            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return head


    
    def swapPairs(self, head):   # just swapping values of node
        temp = head
        while temp:
            if temp.next:
                temp.val, temp.next.val = temp.next.val, temp.val
                temp = temp.next.next
            else:
                break
            
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

    # nh = ll.swapPairs(ll.head)
    nh = ll.swapPairs_pointers(ll.head)

    ll.printList(nh)

