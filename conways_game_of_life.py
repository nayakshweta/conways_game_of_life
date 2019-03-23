def get_array_of_strings_from_file(file_path):
    with open('input_file.txt', 'r') as file:
        return file.readlines()

if __name__ == '__main__':
    lines = get_array_of_strings_from_file('input_file.txt')
    grid = create_grid_from_array_of_strings(lines)

    next_grid = grid.calculate_next_grid()
    create_output_file_from_grid(next_grid)