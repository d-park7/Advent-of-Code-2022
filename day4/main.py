"""
Day 4: Camp Cleanup

Link: https://adventofcode.com/2022/day/3

"""


def full_overlap(pair1, pair2):
    p1 = [int(num) for num in pair1.split("-")]
    p2 = [int(num) for num in pair2.split("-")]
    p1_start = p1[0]
    p1_end = p1[1]
    p2_start = p2[0]
    p2_end = p2[1]

    return (p1_start <= p2_start and p1_end >= p2_end) or (
        p2_start <= p1_start and p2_end >= p1_end
    )


if __name__ == "__main__":
    with open("input.txt") as file:
        pair_list = file.read().splitlines()

    overlap_count = 0
    for pair in pair_list:
        sections = pair.split(sep=",")
        if full_overlap(sections[0], sections[1]):
            overlap_count += 1

    print(f"Overlapping sections: {overlap_count}")
