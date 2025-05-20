#Ui Code:

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
#from PIL import Image
import random

ctk.set_appearance_mode("Dark")           #"Dark", "Light", or "System"
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Dice Roller")
root.geometry("1000x500")
root.resizable(False, False)

greetingtextbox = ctk.CTkLabel(root, text="Hello Welcome To the Dice Roller!", font=("Arial", 12))
greetingtextbox.pack()

#\n\n1. Roll d6.\n 2. Roll d20. \n 3. Roll History.\n 4. Quit.\n
def roll_d6():
    d6 = random.randint(1,6)

    d6Ui.pack()
    print(f"D6: {d6}")
    return(d6)

def roll_d20():
    d20 = random.randint(1,20)
    print(f"D20: {d20}")
    d20Ui = ctk.CTkLabel(root, text=f"D20: {d20}")
    return(d20)


historyframe = ctk.CTkScrollableFrame(root)
historyframe.place(relx=0.5, rely=0.5, anchor="center")

historylabel = ctk.CTkLabel(historyframe, text="Hello Welcome To the Dice Roller!", font=("Arial", 12))
historylabel.pack()


d6button = ctk.CTkButton(root, text=("Roll D6"), command=roll_d6)

d6button.place(relx=0.5, rely=0.1, anchor="center")


d20button = ctk.CTkButton(root, text=("Roll D20"), command=roll_d20)

d20button.place(relx=0.5, rely=0.170, anchor="center")




root.mainloop()

