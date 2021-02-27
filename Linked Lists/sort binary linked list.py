class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None
 
    
    def sortBinaryLinkedList(self, head):
        temp = head
        total_sum = 0
        l = 0
        while temp:
            l += 1
            total_sum += temp.val
            temp = temp.next
        
        zeros_count = l - total_sum
        temp = head
        while temp:
            if zeros_count > 0:
                temp.val = 0
                zeros_count -= 1
            else:
                temp.val = 1
            temp = temp.next

        return head


    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")



if __name__ == "__main__":
    myList = [1]*5
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    ll.head.next.next.next.next = Node(myList[4])
    
    ll.printList(ll.head)

    new_head = ll.sortBinaryLinkedList(ll.head)

    ll.printList(new_head)


