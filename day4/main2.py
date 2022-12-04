"""
Day 4: Camp Cleanup

Link: https://adventofcode.com/2022/day/3

"""


def section_overlap(pair1, pair2):
    p1 = [int(num) for num in pair1.split("-")]
    p2 = [int(num) for num in pair2.split("-")]
    p1_start = p1[0]
    p1_end = p1[1]
    p2_start = p2[0]
    p2_end = p2[1]

    overlap = False

    # Checks if either the start or end of either pair intersects with with the range of the other
    if (p2_start >= p1_start and p2_start <= p1_end) or (
        p1_start >= p2_start and p1_start <= p2_end
    ):
        overlap = True

    return overlap


if __name__ == "__main__":
    with open("input.txt") as file:
        pair_list = file.read().splitlines()

    overlap_count = 0
    for pair in pair_list:
        sections = pair.split(sep=",")
        if section_overlap(sections[0], sections[1]):
            overlap_count += 1

    print(f"Overlapping sections: {overlap_count}")
