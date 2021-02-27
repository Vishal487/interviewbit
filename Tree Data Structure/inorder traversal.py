def inorder(root):
    current = root 
    stack = []
    ans = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left 
        elif(stack):
            current = stack.pop()
            ans.append(current.val)
            current = current.right 
 
        else:
            break
    return ans

