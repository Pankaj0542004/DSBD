def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, num_colors, colors, node=0):
    # If all nodes are colored, return True
    if node == len(graph):
        print("Coloring:", colors)
        return True

    # Try assigning each color to the current node
    for color in range(1, num_colors + 1):
        if is_safe(node, color, graph, colors):
            colors[node] = color  # Assign color
            if graph_coloring(graph, num_colors, colors, node + 1):  # Recur for next node
                return True
            colors[node] = 0  # Backtrack if this color doesn't lead to a solution

    return False

# Define the graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

# Number of colors
num_colors = 3

# Array to store colors of nodes (0 means no color)
colors = [0] * len(graph)

# Solve the graph coloring problem
if not graph_coloring(graph, num_colors, colors):
    print("No solution found")
