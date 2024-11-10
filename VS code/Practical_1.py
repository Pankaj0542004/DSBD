def aStarAlgo(start_node, stop_node):
    open_set = {start_node}  
    closed_set = set() 
    g = {}  
    parents = {}  

    g[start_node] = 0  
    parents[start_node] = start_node #

    while open_set:  
        n = None 
        
        # Node with lowest f() is found
        for v in open_set: 
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):  
                n = v 
                
        if n == stop_node:  
            path = []  
            while parents[n] != n:  
                path.append(n)  
                n = parents[n]  
            path.append(start_node)
            path.reverse()  
            print('Path found: {}'.format(path))  
            return path  

        for (m, weight) in get_neighbors(n):  
            if m not in open_set and m not in closed_set: #if the neighbour_node is not found in open_set or closed_set  
                open_set.add(m)  
                parents[m] = n   
                g[m] = g[n] + weight  
            else:  #if the neighbour_node is found in open_set or closed_set
                if g[m] > g[n] + weight:  
                    g[m] = g[n] + weight  
                    parents[m] = n 
                    if m in closed_set:
                        closed_set.remove(m)  
                        open_set.add(m)  

        open_set.remove(n)  
        closed_set.add(n)	

    print('Path does not exist!')  #if the stop_node not found 
    return None #nothing found 

def get_neighbors(v):  #find the neighbours of particular node
    return Graph_nodes.get(v, [])  

def heuristic(n): #function declaring dictionary of heuristic values given above node 
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist.get(n, float('inf'))  #reurns the particular node's h(n) value till infinity

# Define the graph
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Run the A* algorithm
aStarAlgo('A', 'G')


