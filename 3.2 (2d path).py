from collections import deque
import copy

NOT_FOUND = 1000
NOT_VISITED = 1000
WALL = 1000


def check_inside(cell, map):
    rows = len(map)
    cols = len(map[0])

    if (cell[0] >= 0 and cell[1] >= 0 and cell[0] < rows and cell[1] < cols):
        return True
    else:
        return False


def find_min_length(current_cell, ds, map, lengths):
    previous_length = []

    for d in ds:
        previous_cell = current_cell[0] + d[0], current_cell[1] + d[1]
        if (check_inside(previous_cell, map) and map[previous_cell[0]][previous_cell[1]] == -1
                and map[previous_cell[0]][previous_cell[1]] != WALL):
            previous_length.append(lengths[previous_cell[0]][previous_cell[1]])

    return min(previous_length)


def check_path(cell, map, ds):
    zeros = 0
    for d in ds:
        around_cell = cell[0] + d[0], cell[1] + d[1]
        if (check_inside(around_cell, map) and map[around_cell[0]][around_cell[1]] != WALL):
            zeros += 1
    if zeros > 1:
        return True
    else:
        return False


def find_path(map):
    rows = len(map)
    cols = len(map[0])

    lengths = [[NOT_VISITED] * cols for i in range(rows)]
    lengths[rows - 1][cols - 1] = 1

    possible_paths = set()

    ds = ((0, -1), (-1, 0), (0, 1), (1, 0))

    map_2 = [[(0 if map[i][j] == 0 else WALL) for j in range(cols)]
             for i in range(rows)]

    q = deque()
    q.append((rows - 1, cols - 1))

    while len(q) > 0:
        current_cell = q.popleft()
        if current_cell != (rows - 1, cols - 1):
            lengths[current_cell[0]][current_cell[1]] = find_min_length(
                current_cell, ds, map_2, lengths) + 1

        map_2[current_cell[0]][current_cell[1]] = -1

        if (current_cell == (0, 0)):
            return lengths[0][0], possible_paths

        for d in ds:
            next_cell = current_cell[0] + d[0], current_cell[1] + d[1]
            if (check_inside(next_cell, map_2) and map_2[next_cell[0]][next_cell[1]] != WALL
                    and map_2[next_cell[0]][next_cell[1]] != -1):
                if next_cell not in q:
                    q.append((next_cell[0], next_cell[1]))
            elif (check_inside(next_cell, map_2) and map_2[next_cell[0]][next_cell[1]] == WALL):
                if check_path(next_cell, map_2, ds):
                    possible_paths.add(next_cell)

    return NOT_FOUND, possible_paths


def solution(map):
    res, possible_paths = find_path(map)
    if res != len(map) + len(map[0]) - 1:
        for wall in possible_paths:
            _map = copy.deepcopy(map)
            _map[wall[0]][wall[1]] = 0
            _res = find_path(_map)[0]
            if res > _res:
                res = _res
                if res == len(map) + len(map[0]) - 1:
                    break
    if res == 1000:
        return len(map) + len(map[0]) - 1
    return res


# print(solution([
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]))

# print((solution([
#     [0, 0, 0, 0, 1, 1, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0],
#     [1, 0, 0, 1, 1, 1, 1, 1, 0],
#     [0, 1, 0, 1, 0, 0, 0, 1, 1],
#     [0, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 1, 0]
# ])))

# print(solution([
#     [0, 0, 1, 0, 0, 0],
#     [1, 1, 0, 1, 1, 0],
#     [0, 1, 0, 0, 1, 0],
#     [0, 1, 1, 0, 0, 1],
#     [0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0]]))

# print(solution([
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]))
