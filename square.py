
class Square:
    def __init__(self, black, piece):
        # self.row = row
        # self.col = col
        self.black = black
        self.piece = piece
        self.text_rows = self.get_sketch()

    def get_sketch(self):
        rows = ['+-----------']
        if self.piece.id is not 'E':
            if self.black:
                rows.append('|/ / / / / /')
                rows.append('| / ' + self.piece.text + ' / ')
                rows.append('|/ /' + self.piece.color_text + '/ /')
                rows.append('| / / / / / ')
            else:
                rows.append('|           ')
                rows.append('|   ' + self.piece.text + '   ')
                rows.append('|   ' + self.piece.color_text + '   ')
                rows.append('|           ')
        else:
            if self.black:
                rows.append('|/ / / / / /')
                rows.append('| / / / / / ')
                rows.append('|/ / / / / /')
                rows.append('| / / / / / ')
            else:
                for i in range(4):
                    rows.append('|           ')
        return rows
