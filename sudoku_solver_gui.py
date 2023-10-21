import tkinter as tk
from tkinter import Entry

def is_valid(board, row, col, num):
    # Check if 'num' can be placed in the given 'row' and 'col'
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' can be placed in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # Create a 9x9 grid of Entry widgets for the Sudoku puzzle
        self.grid = [[Entry(root, width=3) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.grid[i][j].grid(row=i, column=j)

        # Add a "Solve" button
        solve_button = tk.Button(root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4)

    def solve_sudoku(self):
        board = self.get_current_board()  # Get the current Sudoku board
        if solve_sudoku(board):
            self.display_solved_board(board)  # Display the solved Sudoku
        else:
            print("No solution exists.")

    def get_current_board(self):
        # Retrieve the Sudoku board from the GUI
        board = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.grid[i][j].get()
                if value:
                    board[i][j] = int(value)
        return board

    def display_solved_board(self, board):
        # Update the GUI to display the solved Sudoku
        for i in range(9):
            for j in range(9):
                self.grid[i][j].delete(0, tk.END)
                self.grid[i][j].insert(0, str(board[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
