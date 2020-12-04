from math import max
def max_path(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.value
    return root.value+max(max_path(root.left), max_path(root.right))