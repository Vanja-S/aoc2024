def partOne(area_map, guard_start):
    pos = guard_start
    direction = "^"
    visited = set()
    while pos[0] in range(len(area_map[0])) and pos[1] in range(len(area_map)):
        visited.add(pos)
        match direction:
            case "^":
                if pos[1] - 1 < 0:
                    break
                elif area_map[pos[1] - 1][pos[0]] == "#":
                    direction = ">"
                else:
                    pos = (pos[0], pos[1] - 1)
            case ">":
                if pos[0] + 1 >= len(area_map[0]):
                    break
                elif area_map[pos[1]][pos[0] + 1] == "#":
                    direction = "v"
                else:
                    pos = (pos[0] + 1, pos[1])
            case "<":
                if pos[0] - 1 < 0:
                    break
                elif area_map[pos[1]][pos[0] - 1] == "#":
                    direction = "^"
                else:
                    pos = (pos[0] - 1, pos[1])
            case "v":
                if pos[1] + 1 >= len(area_map[0]):
                    break
                elif area_map[pos[1] + 1][pos[0]] == "#":
                    direction = "<"
                else:
                    pos = (pos[0], pos[1] + 1)

    return (visited, len(visited))

def partTwo(area_map: list, guard_start, visited: set):


def main():
    area_map = []
    guard_start = (0, 0)  # (x, y)-coordinates
    with open("input.txt", "r") as f:
        y = 0
        for line in f.readlines():
            temp = list(line.strip())
            try:
                guard_start = (temp.index("^"), y)
            except ValueError:
                pass
            area_map.append(temp)
            y += 1
    visited, partOneAnswer = partOne(area_map, guard_start)
    print(f"Part one: {partOneAnswer}")
    print(f"Part two: {partTwo(area_map, guard_start, visited)}")


if __name__ == "__main__":
    main()
