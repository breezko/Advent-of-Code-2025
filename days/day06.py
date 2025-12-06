from pathlib import Path
from utils.aoc import aoc_part
from utils.io import read_input, read_split_by_character
import operator


INPUT_FILE = Path(__file__).parents[1] / "inputs" / "raw" / "day06.txt"


def get_fresh_ranges(ids: list[str]) -> list[int]:
    ranges = []
    for line in ids:
        min, max = line.split("-")
        ranges.append([int(min), int(max)])

    return ranges


"""
--- Day 6: Trash Compactor ---
After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
"""


@aoc_part(day=6, part=1)
def solve_part1():
    lines = read_input(INPUT_FILE).splitlines("\n")
    ops = {
        "+": operator.add,
        "*": operator.mul,
    }
    line_values = [line.split() for line in lines if line.strip()]
    operators = line_values.pop()
    problems = [list(col) for col in zip(*line_values)]
    total = 0
    for i in range(len(problems)):
        op = operators[i]
        problem_result = 1 if op == "*" else 0
        for val in problems[i]:
            problem_result = ops[op](problem_result, int(val))
        total += problem_result
    return total


"""
--- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""


@aoc_part(day=6, part=2)
def solve_part2():
    input = read_input(INPUT_FILE).splitlines()
    ops = {
        "+": operator.add,
        "*": operator.mul,
    }
    width = max(len(line) for line in input)
    lines = [line.ljust(width) for line in input]

    rows = lines[:-1]
    ops_row = lines[-1]

    total_result = 0
    current_result = 0
    current_op = "+"

    for col in range(width):
        ch = ops_row[col]
        if ch in "+*":
            total_result += current_result
            current_op = ch
            current_result = 1 if current_op == "*" else 0

        digits = [row[col] for row in rows if row[col].isdigit()]
        if digits:
            num = int("".join(digits))
            current_result = ops[current_op](current_result, num)

    total_result += current_result

    return total_result


if __name__ == "__main__":
    solve_part1()
    solve_part2()
