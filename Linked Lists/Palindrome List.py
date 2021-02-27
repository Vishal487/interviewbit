class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None

    
    def isPalindrome(self, head):
        temp = head
        lst = []
        while temp:
            lst.append(temp.val)
            temp = temp.next
        n = len(lst)
        i = 0
        j = n-1
        while i<=j:
            if lst[i] != lst[j]:
                return 0
            i += 1
            j -= 1
        return 1

    def reverse(self, head):
        if head == None or head.next == None:
            return head
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

            

    def isPalindrome_better(self, head):
        if head == None or head.next == None:
            return 1
        # find length
        temp = head
        l = 0
        while temp:    # O(n)
            l += 1
            temp = temp.next
        
        mid = l//2
        pointer2 = head
        count = 0
        while count < mid:
            pointer2 = pointer2.next
            count += 1
        # print("pointer2: ", pointer2.val)
        if l%2 != 0:
            pointer2 = pointer2.next
        pointer2 = self.reverse(pointer2)
        pointer1 = head
        while pointer2:
            if pointer1.val != pointer2.val:
                return 0
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return 1
        




    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [10,2,2,100]
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    # ll.head.next.next.next.next = Node(myList[4])
    
    ll.printList(ll.head)

    print(ll.isPalindrome(ll.head))
    print(ll.isPalindrome_better(ll.head))
