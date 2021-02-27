class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def printInorder(root):
    print("in-order traversal : ")
    inorder(root)
    print("\n")


class BSTIterator:
    def __init__(self, root):
        self.lst = []
        self.inorder(root)
        self.curr_index = 0

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.lst.append(root.val)
            self.inorder(root.right)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.curr_index == len(self.lst):
            return 0
        else:
            return 1
        

    # # @return an integer, the next smallest number
    def next(self):
        value = self.lst[self.curr_index]
        self.curr_index += 1
        return value


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)

    bst_it = BSTIterator(root)

    while bst_it.hasNext():
        print(bst_it.next())
