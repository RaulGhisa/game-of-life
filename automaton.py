
class Automaton:
    def __init__(self, state: list[list[int]], rules) -> None:
        self.state: list[list[int]] = state
        self.rules = rules
        self.rows = len(self.state)
        self.cols = len(self.state[0])

    def iterate(self) -> list[int]:
        new_state = self._get_empty_state()

        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                neighbours = self._get_neighbours_around_coord(i, j)
                new_state[i][j] = self.rules(neighbours)

        self.state = new_state

    def _get_neighbours_around_coord(self, i: int, j: int) -> list[list[int]]:
        neighbours = [3 * [0] for _ in range(3)]

        for row, ii in enumerate(range(i - 1, i + 2)):
            for col, jj in enumerate(range(j - 1, j + 2)):
                neighbours[row][col] = self.state[ii][jj]

        return neighbours

    def _get_empty_state(self):
        return [len(self.state[0]) * [0] for _ in range(len(self.state))]
