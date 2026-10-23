import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from reviewer.git_helper import is_git_repository, get_staged_diff
from reviewer.ai_engine import analyze_diff_with_ai

console = Console()

def main():
    console.print(Panel.fit("[bold cyan]🤖 Open AI Code Reviewer & PR Explainer CLI[/bold cyan]\n[dim]Hacktoberfest Edition[/dim]"))

    if not is_git_repository():
        console.print("[bold red]Error:[/bold red] Not inside a Git repository. Run this command inside a git workspace.")
        sys.exit(1)

    diff = get_staged_diff()
    if not diff:
        console.print("[bold yellow]No staged changes detected![/bold yellow]")
        console.print("Stage your changes first using: [bold green]git add <file>[/bold green]")
        sys.exit(0)

    console.print("\n[bold green]✓ Staged changes detected.[/bold green] Analyzing diff with AI Engine...")
    
    with console.status("[bold bright_blue]Running automated code review...[/bold bright_blue]", spinner="dots"):
        review_result = analyze_diff_with_ai(diff)

    console.print("\n" + "─" * 60)
    console.print(Panel(Markdown(review_result), title="[bold green]AI Code Review Feedback[/bold green]", border_style="cyan"))
    console.print("─" * 60 + "\n")

if __name__ == "__main__":
    main()