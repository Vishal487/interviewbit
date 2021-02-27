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


def findCousins(root, node_val):
    def level(root, curr_level, node_val):
        if root is None:
            return 0
        elif root.val == node_val:
            return curr_level

        downlevel = level(root.left, curr_level+1, node_val)
        if downlevel != 0:
            return downlevel
        downlevel = level(root.right, curr_level+1, node_val)
        return downlevel

    def printSpecificLevel(root, level, parent_level_nodes):
        if root is None:
            return
        if level == 1:
            parent_level_nodes.append(root)
        printSpecificLevel(root.left, level-1, parent_level_nodes)
        printSpecificLevel(root.right, level-1, parent_level_nodes)


    level_of_node = level(root, 1, node_val)
    if level_of_node <= 2:
        return []
    else:
        ans = []
        parent_level = level_of_node-1
        parent_level_nodes = []
        printSpecificLevel(root, parent_level, parent_level_nodes)
        for parent in parent_level_nodes:
            if (parent.left and parent.left.val == node_val) or (parent.right and parent.right.val == node_val):
                pass
            else:
                if parent.left:
                    ans.append(parent.left.val)
                if parent.right:
                    ans.append(parent.right.val)
        return ans


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    print(findCousins(root, 9))

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""