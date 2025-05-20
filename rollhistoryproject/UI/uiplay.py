#Ui Code:

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import random

ctk.set_appearance_mode("Dark")           #"Dark", "Light", or "System"
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Dice Roller")
root.geometry("1000x500")
root.resizable(False, False)

greetingtextbox = ctk.CTkLabel(root, text="Hello Welcome To the Dice Roller!", font=("Arial", 12))
greetingtextbox.pack()


rollnumber = 0

def roll_d6():
    global rollnumber
    d6 = random.randint(1,6)
    rollnumber += 1
    d6ui = ctk.CTkLabel(historyframe, text=f"Roll {rollnumber},  D6: {d6}", font=("Arial", 12))
    d6ui.pack()
    print(f"D6: {d6}")
    return d6

def roll_d20():
    global rollnumber
    d20 = random.randint(1,20)
    rollnumber += 1
    d20ui = ctk.CTkLabel(historyframe, text=f"Roll {rollnumber},  D20: {d20}", font=("Arial", 12))
    d20ui.pack()
    print(f"D20: {d20}")
    return d20


historyframe = ctk.CTkScrollableFrame(root)
historyframe.place(relx=0.5, rely=0.5, anchor="center")

historylabel = ctk.CTkLabel(historyframe, text="History:", font=("Arial", 12))
historylabel.pack()


d6button = ctk.CTkButton(root, text=("Roll D6"), command=roll_d6)

d6button.place(relx=0.5, rely=0.1, anchor="center")


d20button = ctk.CTkButton(root, text=("Roll D20"), command=roll_d20)

d20button.place(relx=0.5, rely=0.170, anchor="center")

root.mainloop()

