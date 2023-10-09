import os
import shutil
from rich import print
from rich.console import Console
from rich.progress import Progress


TARGET_FOLDER = "target"
WSGI_FILE = "wsgi.py"
BUILD_FILES = ["app.py"] # example: ["models.py", "dbhandler.py"]
BUILD_FOLDERS = [] # example: ["templates", "static"]
PACKAGES_FOLDER = "env/Lib/site-packages/"


# Initialize the progress bar
console = Console()
progress = Progress()

# create target folder or error if exists
if os.path.exists(TARGET_FOLDER):
    print("[bold red]Error:[/bold red] Target folder already exists")
    exit(1)
else:
    os.mkdir(TARGET_FOLDER)
    print("[bold green]Create Target Folder... ✔[/bold green]")

# copy wsgi file
with progress.console as pconsole:
    pconsole.print("[green]Copying WSGI file... [/green]", end="", style="bold")
    shutil.copyfile(WSGI_FILE, os.path.join(TARGET_FOLDER, WSGI_FILE))
    pconsole.print("[green]✔[/green]", style="bold")

# copy build files
for file in BUILD_FILES:
    with progress.console as pconsole:
        pconsole.print(f"[green]Copying {file}... [/green]", end="", style="bold")
        shutil.copyfile(file, os.path.join(TARGET_FOLDER, file))
        pconsole.print("[green]✔[/green]", style="bold")

# copy build folders
for folder in BUILD_FOLDERS:
    with progress.console as pconsole:
        pconsole.print(f"[green]Copying {folder}... [/green]", end="", style="bold")
        shutil.copytree(folder, os.path.join(TARGET_FOLDER, folder))
        pconsole.print("[green]✔[/green]", style="bold")

# copy packages
with progress.console as pconsole:
    pconsole.print(f"[green]Copying Packages... [/green]", end="", style="bold")
    shutil.copytree(PACKAGES_FOLDER, TARGET_FOLDER, dirs_exist_ok=True)
    pconsole.print("[green]✔[/green]", style="bold")

# done
print("[bold green]Build Done ✔[/bold green]")

    