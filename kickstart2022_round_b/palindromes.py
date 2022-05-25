""""
Solution to Gooogle Kickstart 2022 Round B - Palindromes
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74

got an O(n) solution on first attempt, needed to google around for O(√n).
"""
import math


def get_input():
    """Grabs test cases from standard input"""
    T = int(input())
    cases = []
    for _ in range(T):
        A = int(input())
        cases.append(A)
    return cases


def solve(A):
    """Checks if every integer factor is a palindrome"""
    total = 0
    for i in range(1, int(math.sqrt(A)) + 1):
        factor = A / i
        if factor.is_integer():
            if is_palindrome(int(factor)) and factor != i:
                total += 1
            if is_palindrome(int(i)):
                total += 1

    return total


def is_palindrome(num):
    """Returns True if num is a palindrome"""
    return str(num) == str(num)[::-1]


def main():
    """Calls helper functions to solve each test case"""
    cases = get_input()
    for i, case in enumerate(cases):
        ans = solve(case)
        print(f"Case #{i+1}: {ans}")


if __name__ == "__main__":
    main()
