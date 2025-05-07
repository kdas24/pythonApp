# app.py
import random
from rich import print
from pyfiglet import Figlet

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? Because they used up all their cache.",
]

def tell_joke():
    f = Figlet(font='slant')
    print(f"[bold green]{f.renderText('Joke Time!')}[/bold green]")
    print(f"[bold yellow]{random.choice(jokes)}[/bold yellow]")

if __name__ == '__main__':
    tell_joke()
