import random

ROWS = 5  # 雷区行数
COLS = 5  # 雷区列数
MINES = 5  # 地雷数量

# 初始化雷区
def init_board():
    board = [['0' for _ in range(COLS)] for _ in range(ROWS)]
    visible = [['#' for _ in range(COLS)] for _ in range(ROWS)]
    return board, visible

# 随机布雷
def place_mines(board):
    count = 0
    while count < MINES:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        if board[r][c] == '0':
            board[r][c] = 'M'
            count += 1
            # 更新周围的数字
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nr, nc = r + i, c + j
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != 'M':
                        board[nr][nc] = str(int(board[nr][nc]) + 1)

# 打印当前棋盘
def print_board(visible):
    print("   " + " ".join([f"{j+1:2}" for j in range(COLS)]))
    for i in range(ROWS):
        print(f"{i+1:2} " + " ".join(f"{visible[i][j]:2}" for j in range(COLS)))

# 翻开格子
def reveal(board, visible, r, c):
    if not (0 <= r < ROWS and 0 <= c < COLS) or visible[r][c] != '#':
        return 0

    visible[r][c] = board[r][c]
    if board[r][c] == 'M':
        print("你踩到雷了！游戏结束。")
        return -1

    if board[r][c] == '0':
        visible[r][c] = ' '
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    reveal(board, visible, r + i, c + j)
    return 1

# 检查是否赢得游戏
def check_win(board, visible):
    for i in range(ROWS):
        for j in range(COLS):
            if visible[i][j] == '#' and board[i][j] != 'M':
                return False
    return True

def main():
    board, visible = init_board()
    place_mines(board)
    print("欢迎来到扫雷游戏！")

    while True:
        print_board(visible)
        try:
            r, c = map(int, input("请输入要翻开的格子坐标 (行 列，从1开始)：").split())
            r, c = r - 1, c - 1  # 转换为数组索引
        except ValueError:
            print("请输入有效的数字坐标！")
            continue

        if not (0 <= r < ROWS and 0 <= c < COLS):
            print("输入超出范围，请输入有效的行列值！")
            continue

        result = reveal(board, visible, r, c)
        if result == -1:
            break  # 踩雷
        if check_win(board, visible):
            print("恭喜你，扫雷成功！")
            break

    # 显示完整雷区
    print("完整雷区：")
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    main()
