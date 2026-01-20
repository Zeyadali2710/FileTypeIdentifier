# File Type Identifier

A powerful Python utility that identifies file types by analyzing magic bytes (file signatures) rather than relying on file extensions. This tool provides comprehensive file metadata including type, extension, size, and timestamps with a rich, colorized terminal interface.

## Overview

File Type Identifier uses a comprehensive database of file signatures extracted from Wikipedia's "List of file signatures" to accurately determine file types. It supports 290+ file format signatures, making it highly reliable for identifying files regardless of their extension or naming conventions.

**Key Features:**
- 🔍 Accurate file type identification via magic byte analysis
- 📊 Displays file metadata (size, creation time, modification time, access time)
- 🎨 Rich terminal output with colors and formatting
- 🖱️ Interactive GUI file picker
- 📂 Support for 290+ file formats
- 🔄 Auto-formatted extensions (e.g., `wk4, wk5` for multi-extension formats)

## How It Works

File Type Identifier reads the first 64 bytes of a file and compares the bytes against a database of known file signatures (magic bytes). Each file format has a unique sequence of bytes at a specific offset that identifies it. This approach is much more reliable than checking file extensions, which can be misleading or missing.

### Example Magic Bytes:
- **PNG**: `89 50 4E 47 0D 0A 1A 0A` at offset 0
- **JPEG**: `FF D8 FF` at offset 0
- **GIF**: `47 49 46 38` at offset 0 (identifies both GIF87a and GIF89a)
- **ZIP**: `50 4B 03 04` at offset 0

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. Clone or download the repository:
```bash
cd File\ Type\ Identifier
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install beautifulsoup4 lxml rich
```

## Usage

### Running the File Type Identifier

The program uses an interactive GUI file picker:

```bash
python identifier.py
```

This will:
1. Open a file picker dialog
2. Allow you to select a file
3. Display comprehensive file information including:
   - File path
   - File size (human-readable format)
   - File type (from magic bytes)
   - File extension(s)
   - Creation timestamp
   - Last modified timestamp
   - Last accessed timestamp

### Example Output

```
────────────────────────────────────────────────────────────
File path: /Users/zeyad/Desktop/image.png
File Size: 389.34 KB
────────────────────────────────────────────────────────────
File type: Image encoded in the Portable Network Graphics format
File extension: .png
────────────────────────────────────────────────────────────
Last Modified Time (timestamp): 2026-01-16 21:12:48.123456
Creation Time (timestamp): 2026-01-16 20:55:30.456789
Last Accessed Time (timestamp): 2026-01-21 10:30:15.789012
────────────────────────────────────────────────────────────
```

## Project Structure

```
File Type Identifier/
├── identifier.py              # Main application with GUI and file identification
├── signatures.py              # Database of 290+ file signatures (auto-generated)
├── README.md                  # This file
└── .venv/                     # Virtual environment (after setup)
```

### File Descriptions

#### `identifier.py`
Main application entry point. Features include:
- `read_bytes(path, n=64)`: Reads the first N bytes of a file
- `identify_file_type(path)`: Returns the detected file type
- `identify_file_ext(path)`: Returns the detected file extension(s)
- `convert_size(size_bytes)`: Converts bytes to human-readable format
- `main()`: GUI file picker and display logic

#### `signatures.py`
Auto-generated database containing the `Signature` dataclass and `SIGNATURES` list:
```python
@dataclass(frozen=True)
class Signature:
    name: str          # File type description
    offset: int        # Byte offset where magic bytes appear
    extension: str     # File extension(s)
    magic: bytes       # The magic bytes to match
```

## Advanced Usage

### Supported File Formats (Sample)

The tool supports identification of 290+ file formats including:

**Images**: PNG, JPEG, GIF, TIFF, BMP, WebP, HEIC, OpenEXR, QOI, and more

**Archives**: ZIP, RAR, 7z, Gzip, Bzip2, Xz, LZip, and more

**Documents**: PDF, PostScript, Office formats (OOXML, ODF), and more

**Audio/Video**: MP3, FLAC, WAV, MPEG, and more

**Executables**: ELF, Mach-O, PE (Windows), DOS/MZ, and more

**Databases**: SQLite, HDF5, and more

**Other**: SQLite databases, boot sectors, firmware images, and more

## Signature Database

The signature database (`signatures.py`) contains entries like:

```python
SIGNATURES = [
    Signature("Script or data to be passed to the program following the shebang (#!)", 
              0, "", bytes.fromhex("2321")),
    Signature("Image file encoded in the Graphics Interchange Format (GIF)", 
              0, "gif", bytes.fromhex("474946383761")),
    Signature("Image file encoded in the Portable Network Graphics format", 
              0, "png", bytes.fromhex("89504E470D0A1A0A")),
    Signature("Lotus 1-2-3 spreadsheet (v4, v5) file", 
              0, "wk4, wk5", bytes.fromhex("00001A000210040000000000")),
    # ... 290+ more signatures
]
```

## Dependencies

- **beautifulsoup4**: HTML parsing for Wikipedia extraction
- **lxml**: Fast XML/HTML parsing backend
- **rich**: Terminal formatting with colors and styles

Install all at once:
```bash
pip install beautifulsoup4 lxml rich
```

## Key Concepts

### Magic Bytes (File Signatures)
The first few bytes of a file that uniquely identify its type. These are standardized and reliable indicators of file format, regardless of the file's extension.

### Offset
The byte position where the signature begins. Most signatures start at offset 0 (beginning of file), but some formats have signatures at other positions (e.g., offset 4 or 11).

### File Extension Formatting
Files with multiple valid extensions are automatically formatted with commas:
- `wk4wk5` → `wk4, wk5`
- `ztar z` → `ztar, z`
- Single extensions remain unchanged

## Troubleshooting

### File picker doesn't open
Ensure you have Tkinter installed. On Linux:
```bash
sudo apt-get install python3-tk
```

### "Unknown file type" for a valid file
The file format may not be in the database. You can:
1. Add the signature manually to `signatures.py`

### "Rich" module not found
Reinstall dependencies:
```bash
pip install -r requirements.txt
```

## Performance

- File identification: < 1ms per file (reads only first 64 bytes)
- Database size: ~291 signatures
- Memory usage: Minimal (~1 MB for the entire database)

## Limitations

- Only reads the first 64 bytes, so signatures beyond that offset cannot be detected
- Some file formats don't have unique magic bytes
- Requires exact byte match (no fuzzy matching or heuristics)

## Future Enhancements

Potential improvements:
- [ ] CLI mode without GUI for batch processing
- [ ] Support for signatures beyond 64 bytes
- [ ] Export results to JSON/CSV format
- [ ] Integration with external MIME type databases
- [ ] File recovery/forensics mode
- [ ] Performance optimization for large batch files

## License

This project is open source. Feel free to modify and use for your own purposes.

## Sources

The file signatures database is extracted from:
- [Wikipedia: List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

## Contributing

To contribute improvements:
1. Add new file signatures to signatures.py
3. Test with various file formats

## Author

Created as a Python utility for accurate file type identification.

---

**Last Updated**: January 21, 2026
