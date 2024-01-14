import random
import threading
import time
from automaton import Automaton

from gui import CAGui

# random.seed(42)


def generate_random_state(n=30) -> list:
    state = []
    for _ in range(n):
        state.append(random.sample((0, 1), counts=[n//2, n//2], k=n))

    return state


def generate_empty_state(n=30) -> list:
    return [n * [0] for _ in range(n)]


def get_rules_1d(rule_no: int) -> dict[tuple, int]:
    keys = []
    for i in range(8):
        key = tuple(map(int, tuple((bin(i))[2:].zfill(3))))
        keys.append(key)

    values = str(bin(rule_no)[2:].zfill(8))
    values = list(values)
    values = map(int, values)

    return dict(zip(keys, values))


def game_of_life(cell_slider: list[list[int]]) -> int:
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    rows = len(cell_slider)
    cols = len(cell_slider[0])
    assert rows == cols == 3

    cell = cell_slider[rows//2][cols//2]

    neighbours_count = sum([sum(row) for row in cell_slider])
    neighbours_count -= cell

    if cell:
        if neighbours_count < 2:
            return 0
        if neighbours_count in [2, 3]:
            return 1
        if neighbours_count > 3:
            return 0

    # dead cell
    if neighbours_count == 3:
        return 1

    return 0


def iterate_and_draw(automaton: Automaton, gui: CAGui):
    while True:
        gui.draw_state(automaton.state)
        automaton.iterate()
        time.sleep(0.01)


if __name__ == '__main__':
    state = generate_empty_state(100)

    gosper_gun = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for i in range(len(gosper_gun)):
        for j in range(len(gosper_gun[0])):
            state[20 + i][20 + j] = gosper_gun[i][j]

    # state = generate_random_state(60)
    automaton = Automaton(state=state, rules=game_of_life)

    gui = CAGui(rows=automaton.rows, columns=automaton.cols)
    thread = threading.Thread(target=iterate_and_draw, args=(automaton, gui)).run()
    gui.mainloop()
