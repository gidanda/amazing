from src.mazegen.grid import Grid, N, E, S, W


def render_maze(grid: Grid) -> str:
    lines: list[str] = []
    
    for y in range(grid.height):
        row_top = ""
        for x in range(grid.width):
            row_top += "+" + ("---" if grid.has_wall(x, y, N) else "   ")
        row_top += "+"
        lines.append(row_top)

        row_mid = ""
        for x in range(grid.width):
            row_mid += ("|" if grid.has_wall(x, y, W) else " ") + "   "
        row_mid += ("|" if grid.has_wall(grid.width - 1, y, E) else " ")
        lines.append(row_mid)

    row_bottom = ""
    for x in range(grid.width):
        row_bottom += "+" + ("---" if grid.has_wall(x, grid.height - 1, S) else "   ")
    row_bottom += "+"
    lines.append(row_bottom)

    return "\n".join(lines)