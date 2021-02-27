class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def removeDuplicates(self, head):
        if head == None or head.next == None:
            return head
        
        i = head
        j = head

        while j.next != None:
            if j.val != j.next.val:
                i.val = j.val
                i = i.next
            j = j.next
        i.val = j.val
        i.next = None
        return head



    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [1,1,1,2,2]
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    ll.head.next.next.next.next = Node(myList[4])
    
    ll.printList(ll.head)

    new_head = ll.removeDuplicates(ll.head)

    ll.printList(new_head)
