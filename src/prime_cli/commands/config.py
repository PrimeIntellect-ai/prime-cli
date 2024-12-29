import typer
from rich.console import Console
from rich.table import Table
from ..config import Config

app = typer.Typer(help="Configure the CLI")
console = Console()


@app.command()
def view():
    """View current configuration"""
    config = Config()
    settings = config.view()

    table = Table(title="Prime CLI Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    # Show API key (partially hidden)
    api_key = settings["api_key"]
    if api_key:
        masked_key = f"{api_key[:6]}...{api_key[-4:]}" if len(api_key) > 10 else "***"
    else:
        masked_key = "Not set"
    table.add_row("API Key", masked_key)

    # Show base URL
    table.add_row("Base URL", settings["base_url"])

    console.print(table)


@app.command()
def set_api_key(
    api_key: str = typer.Option(
        ..., prompt="Enter your API key", help="Your Prime Intellect API key"
    ),
):
    """Set your API key"""
    config = Config()
    config.set_api_key(api_key)
    console.print("[green]API key configured successfully![/green]")


@app.command()
def set_base_url(
    url: str = typer.Option(
        ...,
        prompt="Enter the API base URL",
        help="Base URL for the Prime Intellect API",
    ),
):
    """Set the API base URL"""
    config = Config()
    config.set_base_url(url)
    console.print("[green]Base URL configured successfully![/green]")


@app.command()
def reset():
    if typer.confirm("Are you sure you want to reset all settings?"):
        config = Config()
        config.set_api_key("")
        config.set_base_url(Config.DEFAULT_BASE_URL)
        console.print("[green]Configuration reset to defaults![/green]")