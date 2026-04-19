#2進数0001,0010,0100,1000で壁の有無を判別するためそれぞれ定義
N, E, S, W = 1, 2, 4, 8

#全ての方向に壁がある場合は1111として定義
ALL_WALLS = N | E | S | W

#各方向に進んだ時の座標の変化量を定義
DIRECTIONS: dict[int, tuple[int, int]] = {
    N: (0, -1),
    E: (1, 0),
    S: (0, 1),
    W: (-1, 0),
}

#隣接セルの壁を一致させるため各方向の反対方向を定義
OPPOSITE: dict[int, int] = {
    N: S,
    E: W,
    S: N,
    W: E,
}

#壁操作の共通基盤
class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        #初期状態:全セル全方向に壁生成
        self._cells: list[list[int]] = [
            [ALL_WALLS for _ in range(width)] for _ in range(height)
        ]
        self._locked: set[tuple[int, int]] = set()

    #座標(x, y)が迷路の範囲内かどうかを返す
    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    #セルをロックしてアルゴリズムの対象外とする
    def lock(self, x: int, y: int) -> None:
        self._locked.add((x, y))

    #(x, y)がself._lockedに含まれているかを返す
    def is_locked(self, x: int, y: int) -> bool:
        return (x, y) in self._locked

    #(x, y)の上下左右の隣接セルのうち、境界内かつロックされていないものを(nx, ny, direction)のリストで返す
    def neighbors(self, x: int, y: int) -> list[tuple[int, int, int]]:
        neighbor_cells: list[tuple[int, int, int]] = []
        for d in DIRECTIONS:
            dx, dy = DIRECTIONS[d]
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and not self.is_locked(nx, ny):
                neighbor_cells.append((nx, ny, d))
        return neighbor_cells

    #(x, y) から direction 方向の壁を壊す
    def remove_wall(self, x: int, y: int, direction: int) -> None:
        self._cells[y][x] &= ~direction
        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy
        self._cells[ny][nx] &= ~OPPOSITE[direction]

    #セルの値とdirectionのANDを取って、0でなければTrueを返す
    def has_wall(self, x: int, y: int, direction: int) -> bool:
        return bool(self._cells[y][x] & direction)

    #self._cells[y][x]を返す
    def get_cell(self, x: int, y: int) -> int:
        return self._cells[y][x]
