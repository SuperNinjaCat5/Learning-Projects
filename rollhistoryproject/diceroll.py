import random
import os
import sys
import time

folder = "./rollhistoryproject"
os.makedirs(folder, exist_ok=True)
HISTORY_FILE = os.path.join(folder, "rollhistory.txt")

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        for roll in history:
            f.write(roll + "\n")


roll_history = load_history()

while True:
    clear_console()
    input1 = input(" 1. Roll d6.\n 2. Roll d20. \n 3. Roll History.\n 4. Quit.\n")
    if input1.isdigit():
        if input1 == "1":
            randomdigit = random.randint(1, 6)
            roll_history.insert(0, f"d6: {randomdigit}")
            clear_console()
            print("\nd6: ", randomdigit, "\n")
            input("Press Enter to go back...")
        elif input1 == "2":
            randomdigit = random.randint(1, 20)
            roll_history.insert(0, f"d20: {randomdigit}")
            clear_console()
            print("\nd20: ", randomdigit, "\n")
            input("Press Enter to go back...")
        elif input1 == "3":
            clear_console()
            if roll_history:
                for i, roll in enumerate(roll_history):
                    print(f"Roll {i+1},", roll_history[i], "\n")
                input("Press Enter to go back...") 
            else:
                print("No rolls yet.\n")
                input("Press Enter to go back...")
        elif input1 == "4":
            clear_console()
            print("Quitting...\n")
            time.sleep(0.1)
            save_history(roll_history)
            break
    else:
            clear_console()
            print(f"Input misunderstood: '{input1}'\nPlease enter a number between 1 and 4. Also, please be sure to write choice as # not #.\n")
            input("Press Enter to go back...")
