# TicTacToeGUI.py
# spring 2026
# prof. lehman
# tkinter gui for Tic Tac Toe using existing TicTacToe class

import tkinter as tk
from tkinter import messagebox
from TicTacToe import TicTacToe


class TicTacToeGUI:
    def __init__(self, root):
        """Create GUI and start a new game."""
        self.root = root
        self.root.title("Tic Tac Toe")

        # player names
        self.x_name = "Player X"
        self.o_name = "Player O"

        # create game object from existing class
        self.game = TicTacToe(self.x_name, self.o_name)

        # title
        self.title_label = tk.Label(
            root,
            text="Tic Tac Toe",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=10)

        # status label
        self.status_label = tk.Label(
            root,
            text="",
            font=("Arial", 14)
        )
        self.status_label.pack(pady=5)

        # frame for board buttons
        self.board_frame = tk.Frame(root)
        self.board_frame.pack(pady=10)

        # 3x3 button board
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text=" ",
                    width=5,
                    height=2,
                    font=("Arial", 24),
                    command=lambda r=row, c=col: self.button_click(r, c)
                )
                btn.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(btn)
            self.buttons.append(button_row)

        # bottom buttons
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        self.restart_button = tk.Button(
            self.control_frame,
            text="Restart Game",
            font=("Arial", 12),
            command=self.restart_game
        )
        self.restart_button.grid(row=0, column=0, padx=10)

        self.quit_button = tk.Button(
            self.control_frame,
            text="Quit",
            font=("Arial", 12),
            command=root.quit
        )
        self.quit_button.grid(row=0, column=1, padx=10)

        self.update_display()

    def button_click(self, row, col):
        """Handle a board button click."""
        # ignore click if game already over
        if self.game.over():
            return

        # determine symbol to display before play changes turn
        current_turn = self.game.turn

        # only allow play if square is empty
        if self.game.board[row][col] == 0:
            self.game.play(row, col)

            if current_turn == 1:
                self.buttons[row][col]["text"] = "X"
            else:
                self.buttons[row][col]["text"] = "O"

            self.update_display()

            if self.game.over():
                self.end_game()
        else:
            messagebox.showinfo("Invalid Move", "Sorry, that spot is already taken.")

    def update_display(self):
        """Update status label with current turn or game result."""
        if self.game.over():
            winner = self.game.getWinner()
            if winner == "Tie":
                self.status_label.config(text="Game Over: Tie")
            else:
                self.status_label.config(text=f"Game Over: {winner} wins!")
        else:
            self.status_label.config(text=f"It is {self.game.getTurn()}'s turn.")

    def end_game(self):
        """Disable board and show winner."""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["state"] = "disabled"

        winner = self.game.getWinner()
        if winner == "Tie":
            messagebox.showinfo("Game Over", "The game is a tie.")
        else:
            messagebox.showinfo("Game Over", f"{winner} wins!")

    def restart_game(self):
        """Start a new game using the same player names."""
        self.game = TicTacToe(self.x_name, self.o_name)

        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = " "
                self.buttons[row][col]["state"] = "normal"

        self.update_display()


def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()