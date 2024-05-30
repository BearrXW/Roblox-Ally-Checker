import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from time import sleep

# Initialize the console
console = Console()

def fetch_allies(group_id):
    url = f"https://groups.roblox.com/v1/groups/{group_id}/relationships/allies?StartRowIndex=1&MaxRows=10000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['totalGroupCount']
    else:
        console.print(f"[bold red]Error fetching data from Roblox API. Status code: {response.status_code}[/bold red]")
        return None

def main():
    # Display welcome message with animation
    welcome_text = Text("Welcome to the Roblox Allies Counter!", style="bold magenta", justify="center")
    console.print(Panel(welcome_text, border_style="bold green"))

    sleep(1)

    group_id = Prompt.ask("\n[bold yellow]Please enter the Roblox group ID[/bold yellow]")

    # Show fetching allies with progress bar
    console.print("\n[bold yellow]Fetching allies...[/bold yellow]", justify="center")
    for _ in track(range(10), description="Processing..."):
        sleep(0.1)

    total_allies = fetch_allies(group_id)

    if total_allies is not None:
        table = Table(title="Roblox Group Allies Count", title_style="bold green")

        table.add_column("Group ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Total Allies", justify="center", style="magenta")

        table.add_row(group_id, str(total_allies))

        console.print("\n[bold green]Results:[/bold green]", justify="center")
        console.print(table)
        input()

if __name__ == "__main__":
    main()
