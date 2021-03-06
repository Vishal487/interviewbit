class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


from collections import deque
def bfs(root):
    ans = []
    que = deque()
    if not root:
        return ans
    
    ans.append([root.val])

    if root.left:
        que.append(root.left)
    if root.right:
        que.append(root.right)

    while len(que) > 0:
        curr_level = []
        temp_que = deque()
        while len(que) > 0:
            popped = que.popleft()
            curr_level.append(popped.val)
            if popped.left:
                temp_que.append(popped.left)
            if popped.right:
                temp_que.append(popped.right)
        
        que = temp_que
        ans.append(curr_level)
    return ans



def levelOrder_labelled(root):
    def heightOfTree(root):
        if root is None:
            return 0
        else:
            lh = heightOfTree(root.left)
            rh = heightOfTree(root.right)

            return 1+max(lh, rh)

    def printSpecificLevel(root, level, curr_level):
        if root is None:
            return
        if level == 1:
            curr_level.append(root.val)
        printSpecificLevel(root.left, level-1, curr_level)
        printSpecificLevel(root.right, level-1, curr_level)


    height = heightOfTree(root)
    # print("height: ", height)
    ans = []
    for d in range(1, height+1):
        curr_level = []
        printSpecificLevel(root, d, curr_level)
        ans.append(curr_level)
    return ans



if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    print(levelOrder_labelled(root))
    print(bfs(root))

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""