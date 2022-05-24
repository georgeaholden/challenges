""""
Solution to palindromes question **UNFINISHED** 

"""


def get_input():
    """Grabs test cases from standard input"""
    T = int(input())
    cases = []
    for _ in range(T):
        A = int(input)
        cases.append(A)
    return cases


def solve(A):
    """Checks if every integer factor is a palindrome"""
    total = 0
    done = set()
    for i in range(1, A//2):
        factor = A / i
        if factor.is_integer():
            if is_palindrome(int(factor)) and factor not in done:
                total += 1
                done.add(factor)
            if is_palindrome(int(i)) and i not in done:
                total += 1
                done.add(factor)

    return total


def is_palindrome(num):
    """Returns True if num is a palindrome"""
    print(num)
    return str(num) == str(num)[::-1]

def main():
    """Calls helper functions to solve each test case"""
    cases = get_input()
    for i, case in enumerate(cases):
        ans = solve(case)
        print(f"Case #{i}: {ans}")


print(solve(144), "done")