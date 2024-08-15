import tkinter as tk
from tkinter import messagebox
import random

# Define constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

class SlotMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")

        self.balance = tk.IntVar(value=0)
        self.lines = tk.IntVar(value=1)
        self.bet_amount = tk.IntVar(value=1)

        self.create_widgets()

    def create_widgets(self):
        # Balance Label and Entry
        balance_label = tk.Label(self.root, text="Balance:")
        balance_label.pack()
        balance_entry = tk.Entry(self.root, textvariable=self.balance, state="readonly")
        balance_entry.pack()

        # Lines Label and Spinbox
        lines_label = tk.Label(self.root, text="Lines (1-" + str(MAX_LINES) + "):")
        lines_label.pack()
        lines_spinbox = tk.Spinbox(self.root, from_=1, to=MAX_LINES, textvariable=self.lines)
        lines_spinbox.pack()

        # Bet Amount Label and Spinbox
        bet_label = tk.Label(self.root, text="Bet Amount ($" + str(MIN_BET) + "-" + str(MAX_BET) + "):")
        bet_label.pack()
        bet_spinbox = tk.Spinbox(self.root, from_=MIN_BET, to=MAX_BET, textvariable=self.bet_amount)
        bet_spinbox.pack()

        # Spin Button
        spin_button = tk.Button(self.root, text="Spin", command=self.spin_slot_machine)
        spin_button.pack()

    def deposit(self, amount):
        self.balance.set(self.balance.get() + amount)

    def spin_slot_machine(self):
        lines = self.lines.get()
        bet = self.bet_amount.get()
        total_bet = lines * bet

        if total_bet > self.balance.get():
            messagebox.showwarning("Insufficient Balance", "You do not have enough money to bet.")
        else:
            self.balance.set(self.balance.get() - total_bet)
            self.play_game(lines, bet)

    def play_game(self, lines, bet):
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        winnings, winning_lines = check_winning(slots, lines, bet, symbol_values)

        self.deposit(winnings)

        messagebox.showinfo("Game Result", f"You won ${winnings} on lines: {', '.join(map(str, winning_lines))}")
        messagebox.showinfo("New Balance", f"Your new balance is ${self.balance.get()}.")

# Functions from your original code
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Create the main Tkinter window and start the GUI
root = tk.Tk()
app = SlotMachineGUI(root)
root.mainloop()