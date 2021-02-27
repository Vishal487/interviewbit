def preOrder(root):
    ans = []
    stack = []
    stack.append(root)

    while stack:
        curr = stack.pop()
        ans.append(curr.val)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return ans
    