#Ui Code:

import tkinter as tk
import random

root = tk.Tk()
root.title("Pop-up")
root.geometry("1000x500")
root.resizable(False, False)

greetingtextbox = tk.Label(root, text="Hello Welcome To the Dice Roller!", font=("Arial", 12))
greetingtextbox.pack()

#\n\n1. Roll d6.\n 2. Roll d20. \n 3. Roll History.\n 4. Quit.\n
def roll_d6():
    d6 = random.randint(1,6)
    print(f"D6: {d6}")
    return(d6)

def roll_d20():
    d20 = random.randint(1,6)
    print(f"D20: {d20}")
    return(d20)



d6button = tk.Button(root, text=("Roll D6"), command=roll_d6)

d6button.pack()

d20button = tk.Button(root, text=("Roll D20"), command=roll_d20)

d20button.pack()









root.mainloop()
