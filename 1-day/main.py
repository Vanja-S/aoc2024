import collections


def getTotalDistance(list1: list, list2: list):

    list1.sort()
    list2.sort()

    total = sum(abs(x - y) for x, y in zip(list1, list2))
    print(total)
    return total


def getSimilarityScore(list1: list, list2: list):
    ctr = collections.Counter(list2)

    print(sum(x * ctr[x] for x in list1))


def main():
    list1 = []
    list2 = []

    with open("./input.txt") as f:
        for line in f:
            values = line.strip().split("   ")
            if len(values) == 2:  # Ensure there are exactly two columns
                col1, col2 = map(int, values)  # Convert to integers
                list1.append(col1)
                list2.append(col2)

    totalDistance = getTotalDistance(list1, list2)

    getSimilarityScore(list1, list2)


if __name__ == "__main__":
    main()
