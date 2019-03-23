from unittest import TestCase
from grid import Grid

def get_array_of_strings_from_file(file_path):
    with open('input_file.txt', 'r') as file:
        return file.readlines()

def create_grid_from_array_of_strings(lines_unformatted):
    lines = [line.strip() for line in lines_unformatted]
    rows = len(lines)
    columns = len(lines[0])

    grid = Grid(rows, columns)

    r = 0
    c = 0

    while r < rows:
        while c < columns:
            if lines[r][c] == '.':
                grid.mark_cell(r, c, False)
            elif lines[r][c] == '*':
                grid.mark_cell(r, c, True)
            c += 1
        c = 0
        r += 1

    return grid

if __name__ == '__main__':
    lines = get_array_of_strings_from_file('input_file.txt')
    grid = create_grid_from_array_of_strings(lines)

    next_grid = grid.calculate_next_grid()
    create_output_file_from_grid(next_grid)