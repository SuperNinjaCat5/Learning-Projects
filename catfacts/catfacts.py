import requests
import os
import sys
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)  

    if response.status_code == 200:
        data = response.json()
        return data["fact"]
    else:
        return "Failed to get a cat fact."
    
def getuserinput_num():
    clear_console()
    user_input = input("How many cat facts do you want to learn?\n")
    if user_input.isdigit() == False:
        print("Enter a number.\n")
        sys.exit()
    return int(user_input)
        
def gimme_the_facts():
    numbercatsofcats = getuserinput_num()
    clear_console()
    for i in range(numbercatsofcats):
        fact = get_cat_fact()
        if len(fact) < 120:
            print(f"Random Cat fact:\n{fact}\n\n")
            time.sleep(3) 
        else:
            print(f"Random Cat fact:\n{fact}\n\n")
            time.sleep(4)

gimme_the_facts()