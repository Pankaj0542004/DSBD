
# Initial values of Alpha and Beta
MAX, MIN = 10000000, -10000000

def minimax(depth, index, maximizingPlayer, values, alpha, beta):
    # Terminating condition: Check if the depth is the leaf node
    if depth == 3:
        return values[index]

    if maximizingPlayer:
        optimum = MIN
        # Recursion for left and right children
        for i in range(2):  # 0 and 1
            val = minimax(depth + 1, index * 2 + i, False, values, alpha, beta)
            optimum = max(optimum, val)
            alpha = max(alpha, optimum)
            # Alpha-Beta Pruning condition
            if beta <= alpha:
                break
        return optimum
    else:
        optimum = MAX
        # Recursion for left and right children
        for i in range(2):  # 0 and 1
            val = minimax(depth + 1, index * 2 + i, True, values, alpha, beta)
            optimum = min(optimum, val)
            beta = min(beta, optimum)
            # Alpha-Beta Pruning condition
            if beta <= alpha:
                break
        return optimum


if __name__ == "__main__":
    values = [5, 7, 12, 6, 3, 18, -9, 4]
    print("The optimum value is:", minimax(0, 0, True, values, MIN, MAX))