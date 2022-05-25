"""
Solution to Gooogle Kickstart 2022 Round B - Infinity Area
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74
"""
import math

def get_input():
    """Grabs test cases from standard input"""
    T = int(input())
    cases = []
    for _ in range(T):
        R, A, B = input().split()
        R, A, B = int(R), int(A), int(B)
        cases.append((R, A, B))
    return cases


def solve(radius, A, B):
    """Calculates area of circles by looping through each and adding to area"""
    area = 0
    i = 0
    while radius > 0:
        if i % 2 == 0:
            area += math.pi * (radius ** 2)
            radius = radius * A
        else:
            area += math.pi * (radius ** 2)
            radius = radius // B
        i += 1
    return area

def main():
    """Calls helper functions to solve each test case"""
    cases = get_input()
    for i, case in enumerate(cases):
        ans = solve(*case)
        print(f"Case #{i + 1}: {ans}")


if __name__ == "__main__":
    main()
