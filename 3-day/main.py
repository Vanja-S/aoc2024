import re
import math


def uncorruptMemory():

    with open("input.txt") as f:
        memory = f.readlines()

    summation = 0

    for line in memory:
        summation += sum(
            list(
                map(
                    lambda x: math.prod(
                        list(
                            map(
                                lambda y: int(y),
                                x.replace("mul(", "").replace(")", "").split(","),
                            )
                        )
                    ),
                    re.findall(r"mul\(\d{,3},\d{,3}\)", line),
                )
            )
        )
    return summation


def filter_matches(matches, skip):
    filtered = []
    for match in matches:
        if match == "don't()":
            skip = True
        if not skip:
            filtered.append(match)
        if match == "do()":
            skip = False
    return filtered, skip


def uncorruptMemoryWithDoDont():
    with open("input.txt") as f:
        memory = f.readlines()

    summation = 0
    skip = False

    for line in memory:
        instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        filtered_ins, skip = filter_matches(instructions, skip)
        summation += sum(
            math.prod(map(int, match.replace("mul(", "").replace(")", "").split(",")))
            for match in filtered_ins
            if match.startswith("mul(")
        )

    return summation


def main():
    print("Part 1 sum: ", uncorruptMemory())
    print("Part 2 sum: ", uncorruptMemoryWithDoDont())


if __name__ == "__main__":
    main()
