import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winning(colums,lines,bet,values):
    winnings=0
    winnings_lines=[]
    for line in range (lines):
        symbol=colums[0][line]
        for column in colums:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol]*bet
                winnings_lines.append(line+1)

    return winnings,winnings_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    colums=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            values=random.choice(current_symbols)
            current_symbols.remove(values)
            column.append(values)

        colums.append(column)
    return colums

def print_slot_machine(colums):
    for row in range(len(colums[0])):
        for i, column in enumerate(colums):
            if i !=len(colums)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")

        print()

# take amount for deposite from user
def deposit():
    while True:
        amount = input("What amount would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if (amount>0):
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Invalid format, please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Invalid number of lines.")
        else:
            print("Invalid format, please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-{MAX_BET}.")
        else:
            print("Invalid format, please enter a number.")
    return amount


def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"You do not have enough money to bet, your currect balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet eaquls to ${total_bet}.")
    # print(balance,lines)

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_line=check_winning(slots,lines,bet,symbol_values)
    print(f"Your total winning amount is: ${winnings}.")
    print(f"You won on line:", *winning_line)
    return winnings-total_bet

# main function
def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans=input("Press enter to play (q for quit).")
        if ans=="q":
            break
        balance += spin(balance)    

    print(f"You left with ${balance}")



main()

