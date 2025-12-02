from utils.module_importer import load_days

if __name__ == "__main__":
    days = load_days()

    for day_name in sorted(days):
        module = days[day_name]

        # Part 1
        if hasattr(module, "solve_part1"):
            result = module.solve_part1()

        # Part 2
        if hasattr(module, "solve_part2"):
            result = module.solve_part2()

        print()  # blank line between days
