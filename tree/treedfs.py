def dfs(cur_node):
    if cur_node is None:
        return
    
    # print(cur_node.value) 전위 순회 시의 방문 노드 표시
    dfs(cur_node.left)
    # print(cur_node.value) 중위 순회 시의 방문 노드 표시
    dfs(cur_node.right)
    # print(cur_node.value) 후위 순회 시의 방문 노드 표시
    
dfs(root)