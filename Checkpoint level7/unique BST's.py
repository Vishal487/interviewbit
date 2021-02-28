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
    inorder(root)
    print("\n")

def generateTreesUtil(start, end):
    trees = []
    for i in range(start, end):
        for left in generateTreesUtil(start, i):
            for right in generateTreesUtil(i+1, end):
                trees.append(TreeNode(i))
                trees[-1].left = left
                trees[-1].right = right
    return trees if trees else [None]


def generateTrees(A):   # A >= 1
    return generateTreesUtil(1, A+1)



if __name__ == "__main__":    
    node_list = generateTrees(3)
    for root in node_list:
        printInorder(root)

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""