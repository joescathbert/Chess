class Piece:
    piece_x = None
    piece_y = None
    img = None
    piecemovecounter = 0
    name = ""

    def __init__(self, a, b, n):
        self.piece_x = a
        self.piece_y = b
        self.name = n

    def update_piece_position(self, a, b):
        self.piece_x = a
        self.piece_y = b


class Pawn(Piece):
    def possiblemove(self, board, xax, yax, check):
        if board[xax][yax] is None:
            if self.name[0] == "B":
                if self.piecemovecounter == 0:
                    if yax == self.piece_y and xax == self.piece_x + 2:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                if yax == self.piece_y and xax == self.piece_x + 1:
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
            if self.name[0] == "W":
                if self.piecemovecounter == 0:
                    if yax == self.piece_y and xax == self.piece_x - 2:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                if yax == self.piece_y and xax == self.piece_x - 1:
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
        else:
            if self.name[0] == "B":
                if xax == self.piece_x + 1 and (yax == self.piece_y + 1 or yax == self.piece_y - 1) and board[xax][yax].name[0] == "W":
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
            if self.name[0] == "W":
                if xax == self.piece_x - 1 and (yax == self.piece_y + 1 or yax == self.piece_y - 1) and board[xax][yax].name[0] == "B":
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
        return 0


class Rook(Piece):
    def possiblemove(self, board, xax, yax, check):
        if xax == self.piece_x:
            if yax > self.piece_y:
                for i in range(self.piece_y + 1, yax):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]

            elif yax < self.piece_y:
                for i in range(self.piece_y - 1, yax, -1):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
        elif yax == self.piece_y:
            if xax > self.piece_x:
                for i in range(self.piece_x + 1, xax):
                    if board[i][yax] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
            elif xax < self.piece_x:
                for i in range(self.piece_x - 1, xax, -1):
                    if board[i][yax] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
        return 0


class Bishop(Piece):
    def possiblemove(self, board, xax, yax, check):
        if xax < self.piece_x:
            if yax < self.piece_y:
                if self.piece_x - xax == self.piece_y - yax:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x - 1, xax, -1):
                        trouble -= 2
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
            elif yax > self.piece_y:
                if self.piece_x - xax == yax - self.piece_y:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x - 1, xax, -1):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]

        elif xax > self.piece_x:
            if yax < self.piece_y:
                if xax - self.piece_x == self.piece_y - yax:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x + 1, xax):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
            elif yax > self.piece_y:
                if xax - self.piece_x == yax - self.piece_y:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x + 1, xax):
                        trouble += 2
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
        return 0


class Queen(Piece):
    def possiblemove(self, board, xax, yax, check):
        if xax == self.piece_x:
            if yax > self.piece_y:
                for i in range(self.piece_y + 1, yax):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]

            elif yax < self.piece_y:
                for i in range(self.piece_y - 1, yax, -1):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
        elif yax == self.piece_y:
            if xax > self.piece_x:
                for i in range(self.piece_x + 1, xax):
                    if board[i][yax] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
            elif xax < self.piece_x:
                for i in range(self.piece_x - 1, xax, -1):
                    if board[i][yax] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
        elif xax < self.piece_x:
            if yax < self.piece_y:
                if self.piece_x - xax == self.piece_y - yax:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x - 1, xax, -1):
                        trouble -= 2
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
            elif yax > self.piece_y:
                if self.piece_x - xax == yax - self.piece_y:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x - 1, xax, -1):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
        elif xax > self.piece_x:
            if yax < self.piece_y:
                if xax - self.piece_x == self.piece_y - yax:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x + 1, xax):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
            elif yax > self.piece_y:
                if xax - self.piece_x == yax - self.piece_y:
                    trouble = self.piece_x + self.piece_y
                    for i in range(self.piece_x + 1, xax):
                        trouble += 2
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
        return 0


class King(Piece):
    def possiblemove(self, board, xax, yax, check):
        if (xax == self.piece_x - 1 and yax == self.piece_y - 1) or (xax == self.piece_x - 1 and yax == self.piece_y) or (
                xax == self.piece_x - 1 and yax == self.piece_y + 1) or (xax == self.piece_x and yax == self.piece_y + 1) or (
                xax == self.piece_x + 1 and yax == self.piece_y + 1) or (xax == self.piece_x + 1 and yax == self.piece_y) or (
                xax == self.piece_x + 1 and yax == self.piece_y - 1) or (xax == self.piece_x and yax == self.piece_y - 1):
            if board[xax][yax] is None:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
            elif board[xax][yax].name[0] != self.name[0]:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
        return 0


class Horse(Piece):
    def possiblemove(self, board, xax, yax, check):
        if ((self.piece_x - xax == 2 or xax - self.piece_x == 2) and (self.piece_y - yax == 1 or yax - self.piece_y == 1)) or (
                (self.piece_x - xax == 1 or xax - self.piece_x == 1) and (self.piece_y - yax == 2 or yax - self.piece_y == 2)):
            if board[xax][yax] is None:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
            elif board[xax][yax].name[0] != self.name[0]:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
        return 0
