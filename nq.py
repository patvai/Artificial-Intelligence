def solve(self, column, left_diagonal, right_diagonal, queens_placed):
    if queens_placed == self.N:
        self.number_of_solutions += 1
        if self.print_solutions:
            print[(i, j)
            for i, j in enumerate(self.solution_board)]:
                return



    valid_spots = self.all_ones & ~(column | left_diagonal | right_diagonal)
    while valid_spots != 0:
        current_spot = -valid_spots & valid_spots
        self.solution_board.append((current_spot & -current_spot).bit_length() - 1)
        valid_spots ^= current_spot
        self.solve((column | current_spot), (left_diagonal | current_spot) >> 1,
                   (right_diagonal | current_spot) << 1, queens_placed + 1)
        self.solution_board.pop()