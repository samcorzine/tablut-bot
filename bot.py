class Game():
    def __init__(self, board, next_player, winner):
        self.board = board
        self.next_player = next_player
        self.winner = winner

    def defense_pieces_non_king(self):
        pieces = []
        x_counter = 0
        while x_counter < 9:
            y_counter = 0
            while y_counter < 9:
                if self.board[x_counter][y_counter] == 1:
                    pieces.append(Piece(x_counter, y_counter, 1, False))
                y_counter += 1
            x_counter += 1

    def attack_pieces(self):
        pieces = []
        x_counter = 0
        while x_counter < 9:
            y_counter = 0
            while y_counter < 9:
                if self.board[x_counter][y_counter] == -1:
                    pieces.append(Piece(x_counter, y_counter, -1, False)
                y_counter += 1
            x_counter += 1

    def king(self):
        x_counter = 0
        while x_counter < 9:
            y_counter = 0
            while y_counter < 9:
                if self.board[x_counter][y_counter] == 10:
                    return Piece(x_counter, y_counter, 1, True)
                y_counter += 1
            x_counter += 1

    def attack_valid_moves(self):
        attack_pieces = self.attack_pieces_non_king()
        moves = {}
        for piece in attack_pieces:
            moves[(piece.x , piece.y)] = piece.valid_moves(self.board)

    def defense_valid_moves(self):
        defense_pieces = self.defense_pieces()
        defense_pieces.append(self.king())
        moves = {}
        for piece in defense_pieces:
            moves[(piece.x, piece.y)] = piece.valid_moves(self.board)



class Piece():
    def __init__(self, x, y, team, is_king):
        self.x = x
        self.y = y
        self.team = team
        self.is_king = is_king

    def valid_moves(board):
        valid_moves = []
        x_counter = self.x
        while x_counter < 9:
            endx = x_counter + 1
            if board[endx][self.y] == 0:
                if endx != 4, self.y != 4, 4 :
                    valid_moves.append((endx, self.y))
            else:
                break
            x_counter += 1
        x_counter = self.x
        while x_counter >= 0:
            endx = x_counter - 1
            if board[endx][self.y] == 0:
                if endx != 4, self.y != 4, 4:
                    valid_moves.append((endx, self.y))
            else:
                break
            x_counter -= 1
        y_counter = self.y
        while y_counter < 9:
            endy = y_counter + 1
            if board[self.x][endy] == 0:
                if self.x, endy != 4, 4:
                    valid_moves.append((self.x, endy))
            else:
                break
            y_counter += 1
        y_counter = self.y
        while y_counter >= 0:
            endy = y_counter - 1
            if board[self.x][endy] == 0:
                if self.x, endy != 4, 4:
                    valid_moves.append((self.x, endy))
            y_counter -= 1
            else:
                break


class Move():
    def __init__(self, player, startx, starty, endx, endy):
        self.player = player
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
