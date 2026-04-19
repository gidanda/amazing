import random
from mazegen.grid import Grid, N, E, S, W
from mazegen.algorithms.prim import PrimAlgorithm
from app.renderer import render_maze


# テスト1: 小さい迷路
print("=== テスト1: 5x5 seed=42 ===")
grid1 = Grid(5, 5)
rng1 = random.Random(42)
algo1 = PrimAlgorithm(grid1, rng1)
algo1.run()
print(render_maze(grid1))
print()

# テスト2: 同じ seed で再現性の確認
print("=== テスト2: 5x5 seed=42 (再現性チェック) ===")
grid2 = Grid(5, 5)
rng2 = random.Random(42)
algo2 = PrimAlgorithm(grid2, rng2)
algo2.run()
print(render_maze(grid2))
print()

# テスト3: 違う seed
print("=== テスト3: 5x5 seed=99 ===")
grid3 = Grid(5, 5)
rng3 = random.Random(99)
algo3 = PrimAlgorithm(grid3, rng3)
algo3.run()
print(render_maze(grid3))
print()

# テスト4: 大きめの迷路
print("=== テスト4: 10x8 seed=42 ===")
grid4 = Grid(10, 8)
rng4 = random.Random(42)
algo4 = PrimAlgorithm(grid4, rng4)
algo4.run()
print(render_maze(grid4))
print()

# テスト5: 再現性の最終確認
print("=== 再現性チェック ===")
if render_maze(grid1) == render_maze(grid2):
    print("OK: seed=42 の2回の結果が一致")
else:
    print("NG: seed=42 の2回の結果が不一致")