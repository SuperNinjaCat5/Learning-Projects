from rich import print
from rich.progress import track
import os
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()

print("[bold blue]Welcome to the Game![/bold blue]")
for step in track(range(20), description="Loading:"):
    time.sleep(0.1)
clear_console()
print("[bold blue]You wake in a [green]forest.[/green][/bold blue]")
whatdoudo = input("What do you do?\n\n")
print("\n[bold blue]You know...[/bold blue]")
time.sleep(1)
print("[bold]I dont give a [bold red]crap.[/bold red][/bold]")
