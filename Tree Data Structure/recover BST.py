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


class Solution:
    def recoverTree(self, root):
        self.lst = []
        self.inorder(root)
        # print(self.lst)
        sorted_lst = sorted(self.lst)
        ans = []
        for i in range(len(sorted_lst)):
            if sorted_lst[i] != self.lst[i]:
                ans.append(sorted_lst[i])
        return ans

        

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.lst.append(root.val)
            self.inorder(root.right)


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[2])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[0])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)

    sol = Solution()

    ans = sol.recoverTree(root)

    print("ans: ", ans)
