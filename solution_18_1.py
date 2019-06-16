""" Search a maze """

from collections import defaultdict

WHITE, BLACK, ENTRANCE, EXIT = 0, 1, 2, 3


def find_path(maze_array):
    """ Returns a list of (from_square, to_square) tuples """

    # create graph from array
    maze_graph, entrance_node, exit_node = convert_maze_array_to_graph(
        maze_array)

    # starting at entrance, search graph until we get to the exit.
    # BFS

    print(maze_graph)

    def search_maze(position, visited):

        adjacent_nodes = {
            node
            for node in maze_graph[position] if node not in visited
        }

        if exit_node in adjacent_nodes:
            # last step
            return [(exit_node)]
        if not adjacent_nodes:
            # dead end
            return []
        else:
            visited.add(position)
            for node in adjacent_nodes:
                path = search_maze(node, visited)
                if path:
                    return [(node)] + path
            return []

    path = search_maze(entrance_node, set())

    if path:
        path = [entrance_node] + path

    return path


def convert_maze_array_to_graph(maze_array):
    """
	Take an mxn 2D array and convert it to a graph.
	Return explicit references to the start and end nodes.
	(or give them values?)
	O(mn) ?
	"""

    # model graph as adjacency list (hashmap)
    # dictionary of sets
    maze_graph = defaultdict(set)
    entrance_node = None
    exit_node = None
    m = len(maze_array)
    n = len(maze_array[0])

    # iterate through each of the squares
    for i in range(m):
        for j in range(n):
            if (maze_array[i][j] in {WHITE, ENTRANCE, EXIT}
                    and (i, j) not in maze_graph):

                # add any adjacent white squares to this node's
                # adjacency list, and vice versa

                adjacent_nodes = {
                    (i, l)
                    for l in {max(0, j - 1), min(n - 1, j + 1)}
                }.union({
                    (k, j)
                    for k in {max(0, i - 1), min(m - 1, i + 1)}
                })

                for node in adjacent_nodes:
                    if maze_array[node[0]][node[1]] in {WHITE, ENTRANCE, EXIT}:
                        maze_graph[(i, j)].add(node)
                        maze_graph[node].add((i, j))
                if maze_array[i][j] == ENTRANCE:
                    entrance_node = (i, j)
                elif maze_array[i][j] == EXIT:
                    exit_node = (i, j)

    return maze_graph, entrance_node, exit_node