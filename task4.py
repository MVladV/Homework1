# task4

# function for calculating the maximum weight
def pack(W, weights):
 
    rows = len(weights) + 1
    cols = W + 1
    memo_table = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            if weights[i-1] <= j:
                memo_table[i][j] = max(weights[i-1] + memo_table[i-1][j-weights[i-1]], memo_table[i-1][j])
            else:
                memo_table[i][j] = memo_table[i-1][j]
    return memo_table[-1][-1]


def main():
    cap = int(input("Enter capacity: "))
    w = [int(x) for x in input("Enter weight of bars: ").split()]
    print("Result: " + str(pack(cap, w)))

main()
