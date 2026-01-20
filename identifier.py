import math
import os
import sys
from signatures import SIGNATURES
import datetime

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
    if len(sys.argv) != 2:
        print("Usage: python identifier.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_type = identify_file_type(file_path)
    print(f"File Name: {file_path}")
    print(f"File type: {file_type}")
    print(f"File extension: .{identify_file_ext(file_path)}")

    try:
        # Get the stat object
        stat_info = os.stat(file_path)
        lmt_time = datetime.datetime.fromtimestamp(stat_info.st_mtime)
        creation_time = datetime.datetime.fromtimestamp(stat_info.st_ctime)
        access_time = datetime.datetime.fromtimestamp(stat_info.st_atime)


        print(f"File Size : {convert_size(stat_info.st_size)}")
        print(f"Last Modified Time (timestamp): {lmt_time}")
        print(f"Creation Time (timestamp): {creation_time}")
        print(f"Last Accessed Time (timestamp): {access_time}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    main()