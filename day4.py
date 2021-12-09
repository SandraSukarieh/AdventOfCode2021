from pathlib import Path


class Board:
    def __init__(self, board):
        assert len(board) == 5
        assert len(board[0]) == 5
        self.board = [x for x in board]
        self.winner = False
        self.highlighted = [[0 for x in range(5)] for y in range(5)]

    def highlight_cell(self, number):
        for i in range(5):
            for j in range(5):
                if number == self.board[i][j]:
                    self.highlighted[i][j] = 1
                    return

    def check_if_winner(self):
        for i in range(5):
            if self.highlighted[i] == [1, 1, 1, 1, 1]:
                return True
            if [x[i] for x in self.highlighted] == [1, 1, 1, 1, 1]:
                return True
        return False

    def calculate_answer(self, number):
        summed_values = [self.board[i][j] for j in range(5) for i in range(5) if self.highlighted[i][j] == 0]
        return sum(summed_values) * number


# had to add an additional empty line in the input file
def read_input(input_path):
    boards = []
    with open(input_path, "r") as infile:
        numbers = [int(x) for x in infile.readline().split(",")]
        new_board = []
        for line in infile:
            line = line.strip()
            if line:
                new_board.append([int(x) for x in line.strip().split()])
            # if it's the first empty line, do nothing, otherwise save the board and init a new one
            elif len(new_board) != 0:
                assert len(new_board) == 5
                boards.append(Board(new_board))
                new_board = []
    return numbers, boards


def first_task(input_path):
    numbers, boards = read_input(input_path)
    for n in numbers:
        for b in boards:
            b.highlight_cell(n)
            if b.check_if_winner():
                b.winner = True
                print(b.calculate_answer(n))
                return


def second_task(input_path):
    numbers, boards = read_input(input_path)
    scores = []
    for n in numbers:
        for b in boards:
            b.highlight_cell(n)
            if b.check_if_winner() and not b.winner:
                b.winner = True
                scores.append(b.calculate_answer(n))
    print(scores[-1])


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day4.txt')
    first_task(input_path)
    second_task(input_path)
