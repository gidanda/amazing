from mazegen.grid import Grid, N, E, S, W
from app.renderer import render_maze
 
 
# テスト1: 全壁ありの3x2迷路
print("=== テスト1: 全壁あり (3x2) ===")
grid = Grid(3, 2)
print(render_maze(grid))
print()
 
# テスト2: いくつか壁を壊す
print("=== テスト2: 壁を壊す ===")
grid2 = Grid(3, 2)
grid2.remove_wall(0, 0, E)   # (0,0)と(1,0)の間を開通
grid2.remove_wall(1, 0, S)   # (1,0)と(1,1)の間を開通
print(render_maze(grid2))
print()

# テスト3: 通路を作ってみる
print("=== テスト3: 通路を作る (4x3) ===")
grid3 = Grid(4, 3)
grid3.remove_wall(0, 0, E)
grid3.remove_wall(1, 0, E)
grid3.remove_wall(2, 0, S)
grid3.remove_wall(2, 1, S)
grid3.remove_wall(2, 2, W)
grid3.remove_wall(1, 2, W)
print(render_maze(grid3))
print()
 
# テスト4: ロックの確認
print("=== テスト4: ロックセル ===")
grid4 = Grid(4, 3)
grid4.lock(1, 1)  # (1,1)をロック
# ロックセルの neighbors を確認
print(f"(0,1) の隣接セル: {grid4.neighbors(0, 1)}")
print(f"(1,0) の隣接セル: {grid4.neighbors(1, 0)}")
print(f"(1,1) はロック済み: {grid4.is_locked(1, 1)}")
print()
 
# テスト5: 境界チェック
print("=== テスト5: 境界チェック ===")
grid5 = Grid(3, 3)
print(f"(0,0) の隣接セル: {grid5.neighbors(0, 0)}")
print(f"(1,1) の隣接セル: {grid5.neighbors(1, 1)}")
print(f"(2,2) の隣接セル: {grid5.neighbors(2, 2)}")
