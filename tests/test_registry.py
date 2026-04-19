import random
from mazegen.algorithms import get_algorithm, available_algorithms
from mazegen.grid import Grid, N, E, S, W
from app.renderer import render_maze


# テスト1: 登録済みアルゴリズムの一覧
print("=== テスト1: 登録済みアルゴリズム ===")
print(available_algorithms())
print()

# テスト2: 名前からクラスを取得して迷路生成
print("=== テスト2: get_algorithm で Prim を取得 ===")
algo_cls = get_algorithm("prim")
print(f"取得したクラス: {algo_cls}")
grid = Grid(5, 5)
rng = random.Random(42)
algo = algo_cls(grid, rng)
algo.run()
print(render_maze(grid))
print()

# テスト3: 存在しないアルゴリズム名
print("=== テスト3: 存在しないアルゴリズム ===")
try:
    get_algorithm("unknown")
except ValueError as e:
    print(f"期待通りのエラー: {e}")