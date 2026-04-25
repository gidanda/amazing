from collections.abc import Iterator
import random

from mazegen.algorithms import register
from mazegen.algorithms.base import MazeAlgorithm
from mazegen.grid import Grid


@register
class BacktrackerAlgorithm(MazeAlgorithm):
    name: str = "backtracker"

    def __init__(self, grid: Grid, rng: random.Random) -> None:
        super().__init__(grid, rng)

    def steps(self) -> Iterator[tuple[int, int, int]]:
        """Generate maze carving steps using randomized depth-first search.

        Yields:
            Tuples of (x, y, direction), where the wall from cell (x, y)
            toward direction should be removed.
        """
        visited: set[tuple[int, int]] = set()

        start_cell = self._pick_start()
        visited.add(start_cell)

        stack: list[tuple[int, int]] = [start_cell]

        while stack:
            current_cell = stack[-1]
            x, y = current_cell

            unvisited_neighbors: list[tuple[int, int, int]] = []
            for nx, ny, direction in self.grid.neighbors(x, y):
                if (nx, ny) not in visited:
                    unvisited_neighbors.append((nx, ny, direction))

            if unvisited_neighbors:
                nx, ny, direction = self.rng.choice(unvisited_neighbors)

                visited.add((nx, ny))
                stack.append((nx, ny))

                yield x, y, direction
            else:
                stack.pop()