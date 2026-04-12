def gamestate(board: list[str]) -> str:
    x_win = False
    o_win = False
    x_count = sum(line.count("X") for line in board)
    o_count = sum(line.count("O") for line in board)
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")
    if any(line == "XXX" for line in board) or any("".join(line) == "XXX" for line in zip(*board)):
        x_win = True
    if any(line == "OOO" for line in board) or any("".join(line) == "OOO" for line in zip(*board)):
        o_win = True
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] != " ") or (board[0][2] == board[1][1] == board[2][0] != " "):
        if board[1][1] == "X":
            x_win = True
        elif board[1][1] == "O":
            o_win = True
    if x_win and o_win:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_win:
        return "win"
    if o_win:
        return "win"
    if all(" " not in line for line in board):
        return "draw"
    return "ongoing"
