class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None

    def sortedInsert(self, head, new_node):
        if head == None or head.val >= new_node.val:
            new_node.next = head
            head = new_node
        else:
            temp = head
            while temp.next != None and temp.next.val < new_node.val:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        return head

            

    def insertionSortLinkedList(self, head):
        new_head = None
        temp = head
        while temp:
            nextTemp = temp.next
            new_head = self.sortedInsert(new_head, temp)
            temp = nextTemp
        head = new_head
        return head


    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [1,5,3,7,4]   # len = 5
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    ll.head.next.next.next.next = Node(myList[4])
    
    ll.printList(ll.head)

    sorted_head = ll.insertionSortLinkedList(ll.head)

    ll.printList(sorted_head)
    