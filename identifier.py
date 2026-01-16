import sys
from signatures import SIGNATURES

def read_bytes(path: str, n: int = 64) -> bytes:
    with open(path, "rb") as f:
        return f.read(n)

def identify_file_type(path: str) -> str:
    file_bytes = read_bytes(path)
    for signature in SIGNATURES:
        if file_bytes[signature.offset:].startswith(signature.magic):
            return signature.name
    return "Unknown file type"

def main():
    if len(sys.argv) != 2:
        print("Usage: python identifier.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_type = identify_file_type(file_path)
    print(f"File Name: {file_path}")
    print(f"File type: {file_type}")

if __name__ == "__main__":
    main()