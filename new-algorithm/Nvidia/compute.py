class ChessArrayComparator:
    def __init__(self, initial_array):
        self.previous_array = initial_array

    def compare_and_update(self, new_array):
        if self.is_equal(self.previous_array, new_array):
            return "No move occurred"
        else:
            differences = self.find_differences(self.previous_array, new_array)
            move_source_squares = [
                self.get_chess_movement(diff[0], diff[1], diff[2], self.previous_array, new_array)
                for diff in differences
                if self.get_chess_movement(diff[0], diff[1], diff[2], self.previous_array, new_array) is not None
            ]

            if not move_source_squares:
                return "No valid move detected"

            # Sort the source squares based on the source squares themselves and the array index (reversed)
            move_source_squares.sort(key=lambda x: (x.split()[-1], x), reverse=True)

            return "\n".join(move_source_squares)

    def is_equal(self, array1, array2):
        return all(row1 == row2 for row1, row2 in zip(array1, array2))

    def find_differences(self, array1, array2):
        differences = []
        for i, (row1, row2) in enumerate(zip(array1, array2)):
            for j, (elem1, elem2) in enumerate(zip(row1, row2)):
                if elem1 != elem2:
                    differences.append(((i, j), elem1, elem2))
        return differences

    def get_chess_movement(self, position, old_value, new_value, array1, array2):
        row, col = position
        file_char = chr(ord('a') + col)
        rank = 8 - row
        source_square = f"{file_char}{rank}"

        if old_value == 0:
            return f"{source_square} from array 0"
        elif new_value == 0:
            return f"{source_square} from array 1"
        else:
            return None

