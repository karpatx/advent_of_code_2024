# https://github.com/lawrencecraft/AdventOfCode2024/blob/main/day20/day20.py
from typing import List, Tuple, Union

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(raw_input: List[str]):
    print(_get_cheat_count(raw_input, offsets_at_dist(2)))


def part2(raw_input: List[str]):
    print(_get_cheat_count(raw_input, offsets_at_dist(20)))


def _get_cheat_count(input: List[str], cheat_picos: int) -> int:
    mut_maze, coords = _flood_filled_maze(input)
    return sum(_all_cheats(mut_maze, r, c, cheat_picos) for r, c in coords)


def offsets_at_dist(n):
    return [
        (r, c, md)
        for r in range(-n, n + 1)
        for c in range(-n, n + 1)
        if (md := abs(r) + abs(c)) <= n and (r, c) != (0, 0)
    ]


def _all_cheats(
    grid: List[List[Union[str, int]]], r: int, c: int, offsets: List[Tuple[int, int]]
) -> int:
    cheats = 0
    val = grid[r][c]
    thresh = val - 100

    for dr, dc, md in offsets:
        next_r, next_c = r + dr, c + dc

        if (
            0 <= next_r < len(grid)
            and 0 <= next_c < len(grid[r])
            and grid[next_r][next_c] != "#"
            and thresh - md >= grid[next_r][next_c]
        ):
            cheats += 1

    return cheats


def _flood_filled_maze(
    grid: Tuple[str],
) -> Tuple[List[List[Union[str, int]]], List[Tuple[int, int]]]:

    end = _find_guy(grid, "E")

    mut_maze = [list(s) for s in grid]

    q = [(0, end)]

    coords = []

    # flood fill
    while q:
        dist, (r, c) = q.pop(0)

        if isinstance(mut_maze[r][c], int):
            continue

        mut_maze[r][c] = dist
        coords.append((r, c))

        for dr, dc in DIRECTIONS:
            next_r = r + dr
            next_c = c + dc

            if mut_maze[next_r][next_c] == "." or mut_maze[next_r][next_c] == "S":
                q.append((dist + 1, (next_r, next_c)))

    return mut_maze, coords


def _find_guy(map: List[str], char: str) -> Tuple[int, int]:
    for r, l in enumerate(map):
        for c, v in enumerate(l):
            if v == char:
                return r, c

    raise Exception("not here boss")


def main():
    with open("../data/day_20/sample_data.txt", "r") as f:
        stripped_input = [l.strip() for l in f.readlines()]

    part1(stripped_input)
    part2(stripped_input)


if __name__ == "__main__":
    main()