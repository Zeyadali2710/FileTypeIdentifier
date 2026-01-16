# signatures.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Signature:
    name: str
    offset: int
    magic: bytes

SIGNATURES = [
    Signature("PNG image", 0, bytes.fromhex("89504E470D0A1A0A")),
    Signature("ZIP archive", 0, b"PK\x03\x04"),   # local file header
    Signature("PDF document", 0, b"%PDF-"),
    Signature("JPEG image", 0, b"\xFF\xD8\xFF"),
    Signature("GIF image", 0, b"GIF87a"),
    Signature("GIF image", 0, b"GIF89a"),
]