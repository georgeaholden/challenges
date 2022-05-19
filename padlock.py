def main():
    T = int(input())
    results = []
    for i in range(T):
        N, D = input().split()
        N, D = int(N), int(D)
        values = [int(x) for x in input().split()]
        results.append(solve(N, D, values))

    for i, count in enumerate(results):
        print(f"Case #{i+1}: {count}")


def solve(N, D, values):
    left, right = 0, N - 1
    rotations = 0
    while left <= right:
        if values[left] == 0:
            left += 1
        elif values[right] == 0:
            right -= 1
        else:
            left_cost = (cost(values[left], D))
            right_cost = (cost(values[right], D))
            if left_cost <= right_cost:
                rotate(left_cost, values, D, left, right)
                rotations += 1
            else:
                rotate(right_cost, values, D)
                rotations += 1
    return rotations


def rotate(cost, values, D, left, right):
    if cost[1] == "UP":
        for i in range(left, right + 1):
            values[i] = (values[i] + cost[0]) % D
    else:
        for i in range(left, right + 1):
            values[i] = (values[i] - cost[0]) % D


def cost(x, D):
    up_cost = (D + 1) - x
    down_cost = x
    if down_cost <= up_cost:
        return (down_cost, "DOWN")
    else:
        return (up_cost, "UP")


main()