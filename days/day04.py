from pathlib import Path
from utils.aoc import aoc_part
from utils.io import read_input


INPUT_FILE = Path(__file__).parents[1] / "inputs" / "raw" / "day04.txt"


"""
--- Day 4: Printing Department ---
You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
"""


@aoc_part(day=4, part=1)
def solve_part1():
    data = read_input(INPUT_FILE).splitlines()
    SYMBOLS = {"@": 1, ".": 0}

    # Build numeric grid: '@' -> 1, '.' -> 0 (anything else -> 0)
    grid = [[SYMBOLS.get(ch, 0) for ch in line.strip()] for line in data]

    return count_neighbors(grid, False)


def count_neighbors(grid: list, repeat: bool = False):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [
        (-1, 0),  # N
        (-1, 1),  # NE
        (0, 1),  # E
        (1, 1),  # SE
        (1, 0),  # S
        (1, -1),  # SW
        (0, -1),  # W
        (-1, -1),  # NW
    ]

    result = 0
    new_result = 0
    while True:
        new_result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                adj_sum = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        adj_sum += grid[nr][nc]

                if adj_sum < 4:
                    grid[r][c] = 0
                    result += 1
                    new_result += 1
        if not repeat or new_result == 0:
            return result


"""
--- Part Two ---
Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
"""


@aoc_part(day=4, part=2)
def solve_part2():
    data = read_input(INPUT_FILE).splitlines()
    SYMBOLS = {"@": 1, ".": 0}

    # Build numeric grid: '@' -> 1, '.' -> 0 (anything else -> 0)
    grid = [[SYMBOLS.get(ch, 0) for ch in line.strip()] for line in data]

    return count_neighbors(grid, True)


if __name__ == "__main__":
    solve_part1()
    solve_part2()
