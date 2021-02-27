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


def levelOrder(root):
    queue = []
    if root is None:
        return queue
    queue.append(root)
    ans = []
    while queue:
        popped = queue.pop(0)
        # print(popped.val, end=" ")
        ans.append(popped.val)

        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
    return ans

from collections import deque

def reverse_levelOrder(root):
    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue
        ans.appendleft(node.val)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return list(ans)

def reverse_levelOrder_labelled(root):
    def heightOfTree(root):
        if root is None:
            return 0
        else:
            lh = heightOfTree(root.left)
            rh = heightOfTree(root.right)

            return 1+max(lh, rh)

    def printSpecificLevel(root, level, curr_level_nodes):
        if root is None:
            return
        if level == 1:
            curr_level_nodes.append(root.val)
        printSpecificLevel(root.left, level-1, curr_level_nodes)
        printSpecificLevel(root.right, level-1, curr_level_nodes)


    height = heightOfTree(root)
    ans = []
    for d in range(height+1, 0, -1):
        # print("level: ", d)
        curr_level_nodes = []
        printSpecificLevel(root, d, curr_level_nodes)
        ans.extend(curr_level_nodes)
    return ans



if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    # printInorder(root)
    
    print("general level order: ")
    print(levelOrder(root))

    print("reverse level order (iterative): ")
    print(reverse_levelOrder(root))
    
    print("reverse level order: ")
    print(reverse_levelOrder_labelled(root))

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""