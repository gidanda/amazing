from mazegen.algorithms.base import MazeAlgorithm
from collections.abc import Iterator
import random
from mazegen.grid import Grid, OPPOSITE
from mazegen.algorithms import register


@register
class PrimAlgorithm(MazeAlgorithm):
    name: str = "prim"

    def __init__(self, grid: Grid, rng: random.Random) -> None:
        super().__init__(grid, rng)

    def steps(self) -> Iterator[tuple[int, int, int]]:
        #訪問済みのセル、訪問済みセルに隣接する未訪問セルをそれぞれ管理
        visited: set[tuple[int, int]] = set()
        frontier: list[tuple[int, int]] = []

        #ロックされていないセルからランダムに一つ選択        
        start_cell = self._pick_start()
        visited.add(start_cell)

        #開始セルの隣接セルを全てfrontierに追加する
        for nx, ny, d in self.grid.neighbors(*start_cell):
            frontier.append((nx, ny))

        #訪問候補がなくなるまで訪問を繰り返す
        while frontier:
            #frontier からランダムに1つ選んで取り出す。
            # randrange でランダムなインデックスを生成し、popでそのインデックスの要素を削除しつつ取得する
            idx = self.rng.randrange(len(frontier))
            next_cell = frontier.pop(idx)
            #同じセルが複数回 frontier に追加されることがあるため、既に訪問済みならスキップして次の候補へ
            if next_cell in visited:
                continue
            else:
                #新セル (next_cell) の隣接セルのうち、訪問済みのものを集めランダムに1つ選ぶ
                neighbor_cells = self.grid.neighbors(*next_cell)
                neighbor_visited = []
                for nx, ny, d in neighbor_cells:
                    if (nx, ny) in visited:
                        neighbor_visited.append((nx, ny, d))
                nx, ny, d = self.rng.choice(neighbor_visited)
                #壁を壊す指示を返す。dは next_cell → (nx, ny) の方向なので、OPPOSITE[d]で反転して(nx, ny) → next_cellの方向にする。
                #run() がこれを受け取り grid.remove_wall(nx, ny, OPPOSITE[d]) を実行する。
                yield(nx, ny, OPPOSITE[d])
                visited.add(next_cell)
                for x, y, d in self.grid.neighbors(*next_cell):
                    if (x, y) not in visited:
                        frontier.append((x, y))
