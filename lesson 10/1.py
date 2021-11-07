class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        columns = len(self.matrix[0])
        empty_str = "|" + " {} " * columns + "|" + "\n"
        result = ""
        try:
            for row in self.matrix:
                row = empty_str.format(*row)
                result += row
        except IndexError:
            exit("Incorrect matrix")
        return result

    def __add__(self, other):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        try:
            for pos in range(rows):
                for num in range(columns):
                    self.matrix[pos][num] += other[pos][num]
        except IndexError:
            exit("Incorrect matrix to sum")
        return "Summed"