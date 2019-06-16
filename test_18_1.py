from solution_18_1 import find_path, WHITE, BLACK, EXIT, ENTRANCE

def test_2x2_maze():
    maze_array = [[ENTRANCE, WHITE], [BLACK, EXIT]]
    path = find_path(maze_array)
    assert path == [(0, 0), (0, 1), (1, 1)]


def test_4x4_maze():
    maze_array = [[ENTRANCE, WHITE, BLACK, BLACK],
                  [BLACK, WHITE, WHITE, BLACK], [BLACK, BLACK, WHITE, WHITE],
                  [BLACK, BLACK, BLACK, EXIT]]
    path = find_path(maze_array)
    assert path == [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]