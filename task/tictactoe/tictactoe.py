class Game:
    def __init__(self, line):
        arr = [[elem for elem in line[i * 3: (i * 3) + 3]] for i in range(3)]
        if self.is_valid(arr):
            self.field = arr
        else:
            raise ValueError("Field is more or less than 9 cells.")

    @staticmethod
    def is_valid(arr):
        if len(arr) == 3 and len([elem for line in arr for elem in line]) == 9:
            return True

        return False

    def columns(self):
        return [[self.field[j][i] for j in range(3)] for i in range(3)]

    def diagonals(self):
        return [
            [self.field[0][0], self.field[1][1], self.field[2][2]],
            [self.field[0][2], self.field[1][1], self.field[2][0]]
        ]

    def is_possible(self):
        x = len([elem for line in self.field for elem in line if elem == "X"])
        o = len([elem for line in self.field for elem in line if elem == "O"])

        return abs(x - o) <= 1

    def is_empty(self):
        return any(
            [elem != "X" and elem != "O"
             for row in self.field for elem in row]
        )

    def check_winner(self):
        results = self.diagonals() + self.columns() + self.field

        if not self.is_possible() or (["X", "X", "X"] in results and ["O", "O", "O"] in results):
            return "Impossible"
        elif ["X", "X", "X"] in results:
            return "X wins"
        elif ["O", "O", "O"] in results:
            return "O wins"
        elif self.is_empty():
            return "Game not finished"

        return "Draw"

    def draw_field(self):
        print("---------")
        print("| {} {} {} |".format(*self.field[0]))
        print("| {} {} {} |".format(*self.field[1]))
        print("| {} {} {} |".format(*self.field[2]))
        print("---------")

    def check_coordinates(self, coordinates):
        column, row = coordinates

        if column == "/" and row == "/":
            return False

        if not 3 >= column >= 1 or not 3 >= row >= 1:
            print("Coordinates should be from 1 to 3!")
            return False
        elif self.field[abs(row - 3)][column - 1] == '_':
            return True

        print("This cell is occupied! Choose another one!")

        return False

    def make_move(self, symbol='X'):

        move_coordinates = input("Enter the coordinates: ")

        try:
            column, row = [int(item) for item in move_coordinates.split(" ")]
        except ValueError:
            print("You should enter numbers!")
            column, row = "/", "/"

        while not self.check_coordinates([column, row]):
            move_coordinates = input("Enter the coordinates: ")
            try:
                column, row = [int(item) for item in move_coordinates.split(" ")]
            except ValueError:
                print("You should enter numbers!")
                column, row = "/", "/"

        self.field[abs(row - 3)][column - 1] = symbol


field = "_________"
game = Game(field)
moves = 0

while moves < 9 and game.check_winner() == "Game not finished":
    game.draw_field()
    if moves % 2 != 0:
        game.make_move(symbol="O")
    else:
        game.make_move()
    moves += 1

game.draw_field()
print(game.check_winner())
