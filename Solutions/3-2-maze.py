from copy import deepcopy
from time import time
import numpy as np

def print_mat(mat):
    width = len(mat[0])
    height = len(mat)
    for i in range(height):
        row_str = ''
        for j in range(width):
            row_str += '%d ' % mat[i][j]
        print(row_str)
    print('')

def shortest_path(map):
    width = len(map[0])
    height = len(map)
    paths_list = [[(height - 1, width - 1)]]
    for _ in range(10 * max(width, height)):
        new_paths_list = list()
        for path in paths_list:
            last_point = path[-1]
            # Neighboring points
            neighboring_points = [(last_point[0] + i, last_point[1] + j) for i, j in zip([1, 0, -1, 0], [0, 1, 0, -1])]
            # Allowed points (inside the square)
            neighboring_points = [point for point in neighboring_points if point[0] in range(height) and point[1] in range(width)]
            # Allowed points (value 0)
            neighboring_points = [point for point in neighboring_points if map[point[0]][point[1]] == 0]
            # Exclude the path that goes from before (no round trip)
            if len(path) > 1:
                neighboring_points = [point for point in neighboring_points if path[-2] != point]
            for neigh_point in neighboring_points:
                new_paths_list.append(path + [neigh_point])
        paths_list = new_paths_list
        for path in paths_list:
            if (0, 0) in path:
                return len(path)

def solution(map):
    # Your code here
    width = len(map[0])
    height = len(map)
    walls = list()

    # Find all the location of the walls
    for i in range(height):
        for j in range(width):
            if map[i][j] == 1:
                one_neighbors = list()
                for l, k in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                    if i + l in range(height) and j + k in range(width) and map[i + l][j + k] == 1:
                        one_neighbors.append((i + l, j + k))

                if len(one_neighbors) <= 2:
                    walls.append((i, j))

            # if map[i][j] == 1 and not all(map[i + l][j + k] == 1
            #             for l, k in zip([1, 0, -1, 0], [0, 1, 0, -1])
            #             if i + l in range(height) and j + k in range(width)):
            #     walls.append((i, j))
            # if map[i][j] == 1:
            #     walls.append((i, j))

    shortest_paths = list()
    # Remove one wall and compute shorteset path
    for wall in walls:
        tmp_map = deepcopy(map)
        tmp_map[wall[0]][wall[1]] = 0
        # print_mat(tmp_map)
        shortest_paths.append(shortest_path(tmp_map))
    print(f'Number of paths: {len(shortest_paths):d}')
    shortest_paths = [path_length for path_length in shortest_paths if path_length != None]
    return min(shortest_paths)

if __name__ == '__main__':
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]]))

    big_map = np.ones((20, 20))
    big_map[:, 0] = 0
    big_map[-1, :] = 0
    big_map[-1, 0] = 1
    big_map = list(big_map)
    start = time()
    print(solution(big_map))
    print('Time elapsed: %.2e' % (time() - start))

