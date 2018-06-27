class Piece:
    x = None
    y = None
    img = None
    piecemovecounter = 0
    name = ""

    def __init__(self, a, b, n):
        self.x = a
        self.y = b
        self.name = n

    def updatepos(self, a, b):
        self.x = a
        self.y = b


class Pawn(Piece):
    def possiblemove(self, board, xax, yax, check):
        if board[xax][yax] is None:
            if self.name[0] == "B":
                if self.piecemovecounter == 0:
                    if yax == self.y and xax == self.x + 2:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                if yax == self.y and xax == self.x + 1:
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
            if self.name[0] == "W":
                if self.piecemovecounter == 0:
                    if yax == self.y and xax == self.x - 2:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                if yax == self.y and xax == self.x - 1:
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
        else:
            if self.name[0] == "B":
                if xax == self.x + 1 and (yax == self.y + 1 or yax == self.y - 1) and board[xax][yax].name[0] == "W":
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
            if self.name[0] == "W":
                if xax == self.x - 1 and (yax == self.y + 1 or yax == self.y - 1) and board[xax][yax].name[0] == "B":
                    if check == 1: self.piecemovecounter += 1
                    return board[xax][yax]
        return 0


class Rook(Piece):
    def possiblemove(self, board, xax, yax, check):
        if xax == self.x:
            if yax > self.y:
                for i in range(self.y + 1, yax):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]

            elif yax < self.y:
                for i in range(self.y - 1, yax, -1):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
        elif yax == self.y:
            if xax > self.x:
                for i in range(self.x + 1, xax):
                    if board[i][yax] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
            elif xax < self.x:
                for i in range(self.x - 1, xax, -1):
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
        if xax < self.x:
            if yax < self.y:
                if self.x - xax == self.y - yax:
                    trouble = self.x + self.y
                    for i in range(self.x - 1, xax, -1):
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
            elif yax > self.y:
                if self.x - xax == yax - self.y:
                    trouble = self.x + self.y
                    for i in range(self.x - 1, xax, -1):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]

        elif xax > self.x:
            if yax < self.y:
                if xax - self.x == self.y - yax:
                    trouble = self.x + self.y
                    for i in range(self.x + 1, xax):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
            elif yax > self.y:
                if xax - self.x == yax - self.y:
                    trouble = self.x + self.y
                    for i in range(self.x + 1, xax):
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
        if xax == self.x:
            if yax > self.y:
                for i in range(self.y + 1, yax):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]

            elif yax < self.y:
                for i in range(self.y - 1, yax, -1):
                    if board[xax][i] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
        elif yax == self.y:
            if xax > self.x:
                for i in range(self.x + 1, xax):
                    if board[i][yax] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
            elif xax < self.x:
                for i in range(self.x - 1, xax, -1):
                    if board[i][yax] is not None:
                        break
                else:
                    if board[xax][yax] is None:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
                    elif board[xax][yax].name[0] != self.name[0]:
                        if check == 1: self.piecemovecounter += 1
                        return board[xax][yax]
        elif xax < self.x:
            if yax < self.y:
                if self.x - xax == self.y - yax:
                    trouble = self.x + self.y
                    for i in range(self.x - 1, xax, -1):
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
            elif yax > self.y:
                if self.x - xax == yax - self.y:
                    trouble = self.x + self.y
                    for i in range(self.x - 1, xax, -1):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
        elif xax > self.x:
            if yax < self.y:
                if xax - self.x == self.y - yax:
                    trouble = self.x + self.y
                    for i in range(self.x + 1, xax):
                        if board[i][trouble - i] is not None:
                            break
                    else:
                        if board[xax][yax] is None:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
                        elif board[xax][yax].name[0] != self.name[0]:
                            if check == 1: self.piecemovecounter += 1
                            return board[xax][yax]
            elif yax > self.y:
                if xax - self.x == yax - self.y:
                    trouble = self.x + self.y
                    for i in range(self.x + 1, xax):
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
        if (xax == self.x - 1 and yax == self.y - 1) or (xax == self.x - 1 and yax == self.y) or (
                xax == self.x - 1 and yax == self.y + 1) or (xax == self.x and yax == self.y + 1) or (
                xax == self.x + 1 and yax == self.y + 1) or (xax == self.x + 1 and yax == self.y) or (
                xax == self.x + 1 and yax == self.y - 1) or (xax == self.x and yax == self.y - 1):
            if board[xax][yax] is None:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
            elif board[xax][yax].name[0] != self.name[0]:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
        return 0


class Horse(Piece):
    def possiblemove(self, board, xax, yax, check):
        if ((self.x - xax == 2 or xax - self.x == 2) and (self.y - yax == 1 or yax - self.y == 1)) or (
                (self.x - xax == 1 or xax - self.x == 1) and (self.y - yax == 2 or yax - self.y == 2)):
            if board[xax][yax] is None:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
            elif board[xax][yax].name[0] != self.name[0]:
                if check == 1: self.piecemovecounter += 1
                return board[xax][yax]
        return 0
