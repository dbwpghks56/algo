from collections import deque

def levelorder(root):
    maxdepth = 0
    if root is None:
        return maxdepth
    q = deque()
    q.append((root, 1))
    
    while q:
        cur_node, cur_depth = q.popleft
        maxdepth = max(maxdepth, cur_depth)
        
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))
        
    return maxdepth

root = [3,8,20,None,None,15,7]

tree = {}


levelorder(root)