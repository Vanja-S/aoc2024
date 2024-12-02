from math import copysign


def getSafeReports():
    reports = []
    with open("./input.txt") as f:
        for line in f:
            reports.append(list(map(lambda x: int(x), line.strip().split(" "))))

    safeReports = 0

    for report in reports:
        movement = 0
        for i in range(0, len(report) - 1):
            if abs(report[i] - report[i + 1]) == 0:
                break
            elif (
                abs(report[i] - report[i + 1]) >= 1
                and abs(report[i] - report[i + 1]) <= 3
            ):
                if report[i] - report[i + 1] < 0 and (movement == 0 or movement == -1):
                    movement = -1
                elif report[i] - report[i + 1] > 0 and (movement == 0 or movement == 1):
                    movement = 1
                else:
                    break
                if i + 1 == len(report) - 1:
                    safeReports += 1
            else:
                break

    return safeReports


def getTrueSafeReports():
    reports = []

    with open("./input.txt") as f:
        for line in f:
            reports.append(list(map(lambda x: int(x), line.strip().split(" "))))

    safeReports = 0

    for report in reports:
        if is_safe_sequence(report):
            safeReports += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]

            if is_safe_sequence(modified_report):
                safeReports += 1
                break
    return safeReports


def is_safe_sequence(sequence):
    increasing = all(
        sequence[i + 1] - sequence[i] in range(1, 4) for i in range(len(sequence) - 1)
    )
    decreasing = all(
        sequence[i] - sequence[i + 1] in range(1, 4) for i in range(len(sequence) - 1)
    )
    return increasing or decreasing


def main():
    print("Safe reports: ", getSafeReports())
    print("True safe reports: ", getTrueSafeReports())


if __name__ == "__main__":
    main()
