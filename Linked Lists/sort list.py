class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def getMiddle(self, head):
        if  head == None:
            return head
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, left, right):
        result = None

        if left == None:
            return right
        if right == None:
            return left

        if left.val <= right.val:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)

        return result
    
    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        
        middle = self.getMiddle(head)
        nextToMiddle = middle.next

        middle.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddle)

        sortedList = self.sortedMerge(left, right)

        return sortedList


    def insertAtEnd(self, head, n):
        if head == None :
            head = n
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = n
        return head


    def notGoodSol(self, head):
        if head == None or head.next == None:
            return head

        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next
        
        lst.sort()
        head = None
        for e in lst:
            head = self.insertAtEnd(head, Node(e)) 
        return head



    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [1,9,4,2,8]
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    ll.head.next.next.next.next = Node(myList[4])
    
    ll.printList(ll.head)

    # ms = ll.mergeSort(ll.head)

    # ll.printList(ms)

    nh = ll.notGoodSol(ll.head)
    ll.printList(nh)

