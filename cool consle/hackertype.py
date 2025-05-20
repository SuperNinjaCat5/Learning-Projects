from rich import print
from rich.progress import track
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()