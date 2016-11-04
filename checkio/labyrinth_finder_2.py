# CheckIO - Home Challenge 11 : Open Labyrinth
# http://checkio.org

# The labyrinth has no walls, but pits surround the path on each side.
# If a players falls into a pit, they lose.
# The labyrinth is presented as a matrix (a list of lists): 1 is a pit and 0 is part of the path.
# The labyrinth's size is 12 x 12 and the outer cells are also pits.
# Players start at cell (1,1). The exit is at cell (10,10).
# You need to find a route through the labyrinth.
# Input: A labyrinth map as a list of lists with 1 and 0.
# Output: The route as a string that contains "W", "E", "N" and "S".
# Precondition: labyrinth is 12x12 cells


def checkio(maze_map):
    MOVES = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    CARDINALS = ["S", "N", "W", "E"]
    GOAL = (10, 10)
    nodes = [(1, 1)]  # Node: a cell with >1 optional path
    cells = [(1, 1)]  # Coords of cells of path
    path = ""  # String of cardinal points of each movement

    # Repeat until victory!
    while cells[-1] != GOAL:

        # Checking options of current cell
        options = []
        for m in range(0, 4):
            next = {"cardinal": CARDINALS[m], "coords": tuple([x + y for x, y in zip(cells[-1], MOVES[m])])}
            if maze_map[next["coords"][0]][next["coords"][1]] == 0 and cells.count(next["coords"]) == 0:
                options.append(next)

        # If new cell is a bifurcation...
        if len(options) > 1 and nodes.count(cells[-1]) == 0:
            nodes.append(cells[-1])

        # Running path...
        if len(options) > 0:
            path += options[0]["cardinal"]
            cells.append(options[0]["coords"])

        # No options. Go back...
        if len(options) == 0 and cells[-1] != GOAL:
            nodeFound = False
            while nodeFound == False:  # De-running path until nearest node
                path = path[:-1]
                if nodes.count(cells[-2]) > 0:
                    maze_map[cells[-1][0]][cells[-1][1]] = 1  # Blocking blind alley
                    nodes.remove(cells[-2])
                    nodeFound = True
                cells = cells[:-1]

    print("Final Path: " + path)
    return path


if __name__ == '__main__':
    # This code using only for self-checking and not necessary for auto-testing
    def check_route(func, labyrinth):
        MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
        # copy maze
        route = func([row[:] for row in labyrinth])
        pos = (1, 1)
        goal = (10, 10)
        for i, d in enumerate(route):
            move = MOVE.get(d, None)
            if not move:
                print("Wrong symbol in route")
                return False
            pos = pos[0] + move[0], pos[1] + move[1]
            if pos == goal:
                return True
            if labyrinth[pos[0]][pos[1]] == 1:
                print("Player in the pit")
                return False
        print("Player did not reach exit")
        return False


    # These assert are using only for self-testing as examples.
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."
    print("The local tests are done.")