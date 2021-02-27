class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def kReverseList(self, head, k):    # time is O(len_list) and space is O(len_list)
        lst = []
        temp = head
        while temp:   # O(len_list)
            lst.append(temp.val)
            temp = temp.next
        i = 0
        while i < len(lst):   # O(len_list/k)
            sub_list = (lst[i:i+k])[::-1]
            p = 0
            for j in range(i, i+k):  # O(k)
                lst[j] = sub_list[p]
                p += 1
            i += k
        temp = head
        i = 0
        while temp:  # O(len_list)
            temp.val = lst[i]
            i += 1
            temp = temp.next

        return head



    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [1,2,3,4,5,6]
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    ll.head.next.next = Node(myList[2])
    ll.head.next.next.next = Node(myList[3])
    ll.head.next.next.next.next = Node(myList[4])
    ll.head.next.next.next.next.next = Node(myList[5])
    
    ll.printList(ll.head)

    n_head = ll.kReverseList(ll.head, 3)  ## k has to be perfect divisor of len_list

    ll.printList(n_head)
