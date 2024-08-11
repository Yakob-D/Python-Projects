#random module to randomly pick the symbols for a future use in the get_slot_machine_spin
import random

#constant variables for efficient reference
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

#Dictionary storing the characters, and their amount in the slot machine
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#Dictionary storing the prize(value) of each character in the spin machine, these values get multiplied when a player win
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#Function to check if the player won on the spin, it calculates the amount won, and returns 0 if the player didn't win
def check_winnings(columns, lines, bet, values):
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

#Funtion to spin the slot machine
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

#Function to display the columns and rows with better alignment
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,value in enumerate(columns):
            if i != len(columns)-1:
                print(value[row], end = " | ")
            else:
                print(value[row], end = "")
        print()  

#Function to deposit a money, it performs some validations
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

#function to accept number of lines, it performs some validations
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

#Function to accept the bet, provides validation as well
def get_bet(lines, balance):
    max_bet_allowed = balance//lines
    while True:
        bet = input(f"What would you like to bet on each line (${MIN_BET} - ${MAX_BET}) $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                if bet > max_bet_allowed:
                    print(f"You do not have enough balance to bet that amount, your current balance is ${balance}.")
                else:
                    break
            else:
                print("Enter an amount in the range provided.")
        else:
            print("Please enter a number.")
    return bet

#Function to spin the slot and return the amount of money won or lost, to be used in the main function to update the player's balance accordingly
def spin(balance):
    lines = get_number_of_lines();
    bet = get_bet(lines, balance);
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count);
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"YOU WON ${winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        response = input("Press enter to play (Q to Quit).")
        if response.lower() == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()