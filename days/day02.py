from pathlib import Path
from utils.aoc import aoc_part
from utils.io import read_input

INPUT_FILE = Path(__file__).parents[1] / "inputs" / "raw" / "day02.txt"

def tokenize_ranges(line: str) -> list[str]:
    id_ranges = line.split(",")
    return [r.split("-") for r in id_ranges]


"""
--- Day 2: Gift Shop ---
You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.
Adding up all the invalid IDs in this example produces 1227775554.
"""
@aoc_part(day=2, part=1)
def solve_part1():
    data = read_input(INPUT_FILE)
    id_ranges = tokenize_ranges(data)
    return sum_repeated_ids(id_ranges)


"""
--- Part Two ---
The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.
"""
@aoc_part(day=2, part=2)
def solve_part2() -> int:
    data = read_input(INPUT_FILE)
    id_ranges = tokenize_ranges(data)
    return sum_multiple_repeated_ids(id_ranges)

def sum_multiple_repeated_ids(id_ranges: list[tuple[int, int]]) -> int:
    def is_repeated_pattern(n: int) -> bool:
        s = str(n)
        return len(s) > 1 and s in (s + s)[1:-1]
    total = 0
    for start, end in id_ranges:
        start_i = int(start)
        end_i = int(end)
        for n in range(start_i, end_i + 1):
            if is_repeated_pattern(n):
                total += n
    return total


def sum_repeated_ids(id_ranges: list[tuple]) -> int:
    invalid_ids = []
    for start, end in id_ranges:
        for id_num in range(int(start), int(end) + 1):
            id_str = str(id_num)
            length = len(id_str)
            if length % 2 == 0:
                half = length // 2
                if id_str[:half] == id_str[half:]:
                    invalid_ids.append(id_num)
    return sum(invalid_ids)

if __name__ == "__main__":
    solve_part1()
    solve_part2()