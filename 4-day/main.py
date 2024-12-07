def count_xmas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    xmas = list("XMAS")
    count = 0

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_direction(start_r, start_c, dr, dc):
        if is_valid(start_r + dr * 3, start_c + dc * 3):
            if all(
                grid[start_r + i * dr][start_c + i * dc] == xmas[i] for i in range(4)
            ):
                return True
        return False

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1
                if check_direction(r, c, -dr, -dc):
                    count += 1

    return count


def isXMASPattern(grid, i, j) -> bool:
    # The possible X-MAS patterns are:
    # M  S
    #   A
    # M  S
    #
    # M  M
    #   A
    # S  S
    #
    # S  M
    #   A
    # S  M
    #
    # S  S
    #   A
    # M  M
    # We check the grid for them

    xmas_grid = [
        (-1, 1),
        (1, 1),
        (0, 0),
        (-1, -1),
        (1, -1),
    ]

    # Check the M patterns
    # S  S
    #   A
    # M  M
    if grid[i - 1][j - 1] == "M" and grid[i - 1][j + 1] == "M":
        if grid[i + 1][j - 1] == "S" and grid[i + 1][j + 1] == "S":
            return True
    # M  S
    #   A
    # M  S
    elif grid[i - 1][j - 1] == "M" and grid[i + 1][j - 1] == "M":
        if grid[i - 1][j + 1] == "S" and grid[i + 1][j + 1] == "S":
            return True
    # M  M
    #   A
    # S  S
    elif grid[i + 1][j + 1] == "M" and grid[i + 1][j - 1] == "M":
        if grid[i - 1][j - 1] == "S" and grid[i - 1][j + 1] == "S":
            return True
    # S  M
    #   A
    # S  M
    elif grid[i + 1][j + 1] == "M" and grid[i - 1][j + 1] == "M":
        if grid[i - 1][j - 1] == "S" and grid[i + 1][j - 1] == "S":
            return True

    return False


def countXMASPatterns(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == "A" and isXMASPattern(grid, i, j):
                count += 1

    return count


def main():
    grid = []
    with open("input.txt") as f:
        for line in f:
            grid.append(list(line.strip()))

    print(f"Part 1: {count_xmas_occurrences(grid)}")
    print(f"Part 2: {countXMASPatterns(grid)}")


if __name__ == "__main__":
    main()
