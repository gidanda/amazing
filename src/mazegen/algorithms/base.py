from abc import ABC, abstractmethod
from collections.abc import Iterator
import random
from mazegen.grid import Grid

#迷路生成アルゴリズムの抽象基底クラス
#各アルゴリズムはsteps()を実装し、壁を壊すステップのイテレータを返す
class MazeAlgorithm(ABC):
    name: str = "base"

    #rngはrandom.Randomクラスのインスタンスで、ランダムな選択をするためのもの
    def __init__(self, grid: Grid, rng: random.Random) -> None:
        self.grid = grid
        self.rng = rng

    #迷路生成の開始地点をランダムに選択する
    def _pick_start(self) -> tuple[int, int]:
        not_locked = []
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                if not self.grid.is_locked(x, y):
                    not_locked.append((x, y))
        return self.rng.choice(not_locked)

    @abstractmethod
    def steps(self) -> Iterator[tuple[int, int, int]]:
        ...

    def run(self) -> None:
        for x, y, direction in self.steps():
            self.grid.remove_wall(x, y, direction)
