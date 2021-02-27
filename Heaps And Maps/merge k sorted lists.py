import heapq


class Node:
    def __init__(self, v):
        self.val = v  
        self.next = None  


class ListNode:
    def __init__(self): 
        self.head = None


    def mergeList(self, headList):
        pq = []
        heapq.heapify(pq)
        for i in range(len(headList)):
            temp = headList[i]
            if temp:
                heapq.heappush(pq, (temp.val, temp))
        # print(pq)
        value, tmp = heapq.heappop(pq)
        ans_head = Node(value)
        temp = ans_head
        while len(pq) != 0:
            if tmp.next:
                heapq.heappush(pq, (tmp.next.val, tmp.next))
            value, tmp = heapq.heappop(pq)
            temp.next = Node(value)
            temp = temp.next
        tmp = tmp.next
        while tmp:
            temp.next = tmp
            temp = temp.next
            tmp = tmp.next

        return ans_head



    def printList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("NULL\n")

if __name__ == "__main__":
    myList = [1,6]
    ll = ListNode()
    ll.head = Node(myList[0])
    ll.head.next = Node(myList[1])
    # ll.head.next.next = Node(myList[2])
    # ll.head.next.next.next = Node(myList[3])
    # ll.head.next.next.next.next = Node(myList[4])

    myList = [4,11,13]
    ll2 = ListNode()
    ll2.head = Node(myList[0])
    # ll2.head.next = Node(myList[1])
    # ll2.head.next.next = Node(myList[2])
    # ll2.head.next.next.next = Node(myList[3])

    # myList = [3,8,9]
    # ll3 = ListNode()
    # ll3.head = Node(myList[0])
    # ll3.head.next = Node(myList[1])
    # ll3.head.next.next = Node(myList[2])
    # ll3.head.next.next.next = Node(myList[3])

    
    ll.printList(ll.head)
    ll2.printList(ll2.head)
    # ll3.printList(ll3.head)

    nh = ll.mergeList([ll.head, ll2.head])

    ll.printList(nh)

