def kthSmallest(root, k):
    l=[]
    def ino(root):
        if len(l)==B:
            return
        if root:
            ino(root.left)
            l.append(root.val)
            ino(root.right)
    ino(A)
    return l[B-1]

