def bfs(adjacency_list, start_node):
    # write your code here...
    queue = []
    queue.append(start_node)
    visited = {}
    visited = [start_node]
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for node in adjacency_list[vertex]:
            if node not in visited:
                visited.append(node)
                queue.append(node)




if __name__ == '__main__':
    # take inputs...
    adjacency_list = {
        "a" : set(["b","c"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e"]),
        "e" : set(["a"])
    }
    
    start_node = "a"
    
    print(bfs(adjacency_list, start_node))
