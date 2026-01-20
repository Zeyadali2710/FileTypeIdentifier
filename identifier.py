import math
import os
import sys
from signatures import SIGNATURES
import datetime
from rich import print
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def read_bytes(path: str, n: int = 64) -> bytes:
    with open(path, "rb") as f:
        return f.read(n)

def identify_file_type(path: str) -> str:
    file_bytes = read_bytes(path)
    for signature in SIGNATURES:
        if file_bytes[signature.offset:].startswith(signature.magic):
            return signature.name
    return "Unknown file type"

def identify_file_ext(path: str) -> str:
    file_bytes = read_bytes(path)
    for signature in SIGNATURES:
        if file_bytes[signature.offset:].startswith(signature.magic):
            return signature.extension
    return "Unknown file extension"

def convert_size(size_bytes):
    """
    Convert a file size from bytes to a human-readable format (e.g., KB, MB, GB, TB).
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def main():
    print("Select a file to identify its type and metadata.")

    Tk().withdraw()
    file_path = askopenfilename()
    file_type = identify_file_type(file_path)

    try:
        stat_info = os.stat(file_path)
        lmt_time = datetime.datetime.fromtimestamp(stat_info.st_mtime)
        creation_time = datetime.datetime.fromtimestamp(stat_info.st_ctime)
        access_time = datetime.datetime.fromtimestamp(stat_info.st_atime)
        
        print("-----------------------------------"*2)
        print(f"[bold]File path:[/bold] [underline cyan]{file_path}[/underline cyan]")
        print(f"[bold]File Size: [/bold][underline cyan]{convert_size(stat_info.st_size)}[/underline cyan]")
        
        print("-----------------------------------"*2)
        print(f"[bold]File type:[/bold] [underline bold red]{file_type}[/underline bold red]")
        print(f"[bold]File extension: [/bold][underline bold red].{identify_file_ext(file_path)}[/underline bold red]")
        print("-----------------------------------"*2)
        print(f"[bold]Last Modified Time (timestamp): [/bold][cyan]{lmt_time}[/cyan]")
        print(f"[bold]Creation Time (timestamp): [/bold][cyan]{creation_time}[/cyan]")
        print(f"[bold]Last Accessed Time (timestamp): [/bold][cyan]{access_time}[/cyan]")
        print("-----------------------------------"*2)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    main()