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

        return prev
       
    
    def subtract(self, head):
        if head == None or head.next == None:
            return head
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        mid = l//2
        
        last_half = head
        cnt = 1
        while cnt < mid:
            cnt += 1
            last_half = last_half.next
        # print(last_half.val)
        if l%2 != 0:
            last_half = last_half.next
        temp_last_half = last_half
        last_half.next = self.reverse(last_half.next)

        # print("last half reversed: ")
        # self.printList(last_half.next)

        temp1 = head
        temp2 = last_half.next
        while temp1 and temp2:
            temp1.val = temp2.val - temp1.val 
            temp1 = temp1.next
            temp2 = temp2.next 

        temp_last_half.next = self.reverse(temp_last_half.next)

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
    
    ll.printList(ll.head)

    h = ll.subtract(ll.head)

    ll.printList(h)

"""
1->2->3->5->4
"""