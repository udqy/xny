from rich.console import Console
from rich.markdown import Markdown

def display(file_path):
    console = Console()
    with open(file_path, "r") as f:
        markdown_text = f.read()
    markdown = Markdown(markdown_text)
    console.print(markdown)