# DiceGUI.py
# spring 2026
# lehman
# tkinter gui using two Dice objects

import tkinter as tk
from tkinter import messagebox
from Dice import Dice


class DiceGUI:
    def __init__(self, root):
        """Create GUI window and setup dice objects."""
        self.root = root
        self.root.title("Dice Roller")

        # create two Dice objects
        self.die1 = Dice("Red", 1)
        self.die2 = Dice("Blue", 1)

        # create menu
        self.create_menu()

        # heading
        self.title_label = tk.Label(
            root,
            text="Dice Roller",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=10)

        # frame for dice displays
        self.dice_frame = tk.Frame(root)
        self.dice_frame.pack(pady=10)

        self.die1_label = tk.Label(
            self.dice_frame,
            text=f"{self.die1.id}: {self.die1.get_value()}",
            font=("Arial", 14),
            width=12
        )
        self.die1_label.grid(row=0, column=0, padx=20)

        self.die2_label = tk.Label(
            self.dice_frame,
            text=f"{self.die2.id}: {self.die2.get_value()}",
            font=("Arial", 14),
            width=12
        )
        self.die2_label.grid(row=0, column=1, padx=20)

        # frame for roll buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.roll_die1_button = tk.Button(
            self.button_frame,
            text="Roll Red",
            width=12,
            command=self.roll_die1
        )
        self.roll_die1_button.grid(row=0, column=0, padx=5, pady=5)

        self.roll_die2_button = tk.Button(
            self.button_frame,
            text="Roll Blue",
            width=12,
            command=self.roll_die2
        )
        self.roll_die2_button.grid(row=0, column=1, padx=5, pady=5)

        self.roll_both_button = tk.Button(
            self.button_frame,
            text="Roll Both",
            width=12,
            command=self.roll_both
        )
        self.roll_both_button.grid(row=0, column=2, padx=5, pady=5)

        # total display
        self.total_label = tk.Label(
            root,
            text="Total:",
            font=("Arial", 14)
        )
        self.total_label.pack(pady=(15, 5))

        self.total_text = tk.Text(root, height=1, width=10, font=("Arial", 14))
        self.total_text.pack(pady=5)

        # max rolled display
        self.max_label = tk.Label(
            root,
            text="Highest Roll Seen by Any Die: 0",
            font=("Arial", 12)
        )
        self.max_label.pack(pady=10)

        # initialize display
        self.update_display()

    def create_menu(self):
        """Create menu bar."""
        menu_bar = tk.Menu(self.root)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        game_menu.add_command(label="Reset", command=self.reset_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.exit_game)

        menu_bar.add_cascade(label="Game", menu=game_menu)
        self.root.config(menu=menu_bar)

    def update_display(self):
        """Update die labels, total box, and max rolled label."""
        self.die1_label.config(text=f"{self.die1.id}: {self.die1.get_value()}")
        self.die2_label.config(text=f"{self.die2.id}: {self.die2.get_value()}")

        total = self.die1.get_value() + self.die2.get_value()
        self.total_text.delete("1.0", tk.END)
        self.total_text.insert(tk.END, str(total))

        self.max_label.config(
            text=f"Highest Roll Seen by Any Die: {self.die1.get_maxRolled()}"
        )

    def roll_die1(self):
        """Roll only die 1."""
        self.die1.roll()
        self.update_display()

    def roll_die2(self):
        """Roll only die 2."""
        self.die2.roll()
        self.update_display()

    def roll_both(self):
        """Roll both dice."""
        self.die1.roll()
        self.die2.roll()
        self.update_display()

    def reset_game(self):
        """Reset both dice to 1 and clear shared maxRolled."""
        self.die1.set_value(1)
        self.die2.set_value(1)
        Dice.maxRolled = 0
        self.update_display()
        messagebox.showinfo("Reset", "The game has been reset.")

    def exit_game(self):
        """Close the program."""
        self.root.destroy()
    

def main():
    root = tk.Tk()
    app = DiceGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()