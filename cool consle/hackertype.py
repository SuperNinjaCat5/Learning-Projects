from rich import print
from rich.progress import track
import random
import string
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()

def generate_hack_text_lines(num_lines=50, line_length=60):
    chars = string.ascii_letters + string.digits + string.punctuation + " "
    lines = []
    for _ in range(num_lines):
        line = ''.join(random.choice(chars) for _ in range(line_length))
        lines.append(line)
    return lines

hack_lines = generate_hack_text_lines(50, 60)

for line in track(
    hack_lines,
    description="[bold green]Hacking in progress...[/bold green]",
    style="green",
    complete_style="bold green"
):
    print(f"[bold green]{line}[/bold green]")
    if random.random() < 0.3:  # 30% chance to add blank lines
        print("\n" * random.randint(1, 3))
    time.sleep(0.2)