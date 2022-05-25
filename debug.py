"""
Looking through a ton of test cases to find one or two errors is super difficult.
But I don't want to have to rewrite my answers to write to a file instead of
printing to stdout every single time.

To see how this module works, go break palindromes or something:
change line 23 from:

for i in range(1, int(math.sqrt(A)) + 1):

to

for i in range(1, int(math.sqrt(A))):
"""
from kickstart2022_round_b import palindromes


def compare_results(input_txt, correct_txt, module, google=True):
    """Takes two filenames, input_txt and correct_txt and compares
    the correct answers against output produced by given solver module.
    Parameter google is a bool flag used to determine if input_txt is in
    google kickstart input format (with first line giving T test cases)"""
    inputs = [int(line.strip()) for line in get_content(input_txt)]
    stack = inputs[:]
    expected_results = get_content(correct_txt)
    actual_results = []


    module.print = lambda s: actual_results.append(s)
    module.input = lambda: stack.pop(0)
    module.main()

    print_comparisons(inputs, expected_results, actual_results, google)


def get_content(filename):
    """Returns a list of lines in given file"""
    infile = open(filename)
    content = infile.readlines()
    infile.close()
    return [line.strip() for line in content if len(line.strip()) != 0]


def print_comparisons(inputs, expected_results, actual_results, google):
    """Checks each test case and prints to user if failed"""
    error_count = 0
    for i, case in enumerate(expected_results):
        try:
            assert case == actual_results[i]
        except AssertionError:
            print(f"Case {i+1} failed")
            if google:
                print_input(inputs, i)
            print("-- Expected -- :\n" + case)
            print("-- Got -- :\n" + actual_results[i])
            print()
            error_count += 1
    if error_count == 0:
        print('-- Finished without any errors --')
    elif error_count == 1:
        print('!** Finished with 1 error **!')
    else:
        print(f'!** Finished with {error_count} errors **!')


def print_input(inputs, i):
    """Assuming input_txt follows the format used in Google Kickstart programming
    contests, the first line will contain a single int T which is the number
    of test cases. This function prints the ith test case in inputs
    (Importantly where the first case is at i = 0)"""
    T = int(inputs[0])
    case_length = (len(inputs) - 1) // T
    start_index = (i * case_length) + 1
    end_index = (i * case_length) + 1 + case_length
    print("-- Input -- ")
    for line in inputs[start_index:end_index]:
        print(line)


if __name__ == '__main__':
    in_filename = "kickstart2022_round_b/palindrome_answers/ts1_input.txt"
    out_filename = "kickstart2022_round_b/palindrome_answers/ts1_output.txt"
    compare_results(in_filename, out_filename, palindromes)
