"""
Solution to Gooogle Kickstart 2022 Round B - Unlock the Padlock
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74

Passes test set 1 for 10 pts but greedy approach fails on diff data sets
need to relearn dp I guess lol


George Holden
19/5/2022
"""


def main():
    """Takes T tests cases from standard input and calls solve method"""
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
    """Implements a greedy algorithm, pick closest edge to 0 and rotate
    in corresponding direction"""
    left, right = 0, N - 1
    rotations = 0
    while left <= right:
        if values[left] == 0:
            left += 1
        elif values[right] == 0:
            right -= 1
        else:
            left_cost = (calculate_cost(values[left], D))
            right_cost = (calculate_cost(values[right], D))
            if left_cost <= right_cost:
                rotate(left_cost, values, D, left, right)
                rotations += 1
            else:
                rotate(right_cost, values, D, left, right)
                rotations += 1
    return rotations


def rotate(cost, values, D, left, right):
    """Rotates cost amount in given direction, modifies list values in place"""
    if cost[1] == "UP":
        for i in range(left, right + 1):
            values[i] = (values[i] + cost[0]) % D
    else:
        for i in range(left, right + 1):
            values[i] = (values[i] - cost[0]) % D


def calculate_cost(x, D):
    """Computes a cost value, distance from 0.
    E.g. if D = 3, and x = 1, could spin down once or up twice to reach 0"""
    up_cost = (D + 1) - x
    down_cost = x
    if down_cost <= up_cost:
        return (down_cost, "DOWN")
    else:
        return (up_cost, "UP")


main()
