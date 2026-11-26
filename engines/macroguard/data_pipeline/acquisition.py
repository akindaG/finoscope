"""Reproducible, URL-configurable acquisition of a source CSV file."""
from __future__ import annotations

import argparse
import hashlib
import os
import tempfile
from pathlib import Path
from urllib.request import Request, urlopen


def download_file(url: str, destination: str | Path, *, expected_sha256: str | None = None) -> str:
    """Download a file to destination and return its SHA-256.

    The URL must be supplied explicitly after checking the publisher's terms.
    Downloads are streamed to a temporary file and atomically moved into place.
    """
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()

    request = Request(url, headers={"User-Agent": "FINOSCOPE-MACROGUARD/0.1"})
    temp_name: str | None = None
    try:
        with urlopen(request, timeout=60) as response:
            with tempfile.NamedTemporaryFile(
                mode="wb", dir=target.parent, prefix=f".{target.name}.",
                suffix=".part", delete=False
            ) as temporary:
                temp_name = temporary.name
                while chunk := response.read(1024 * 1024):
                    digest.update(chunk)
                    temporary.write(chunk)

        actual_sha256 = digest.hexdigest()
        if expected_sha256 and actual_sha256.lower() != expected_sha256.lower():
            raise ValueError(
                f"SHA-256 mismatch: expected {expected_sha256}, got {actual_sha256}"
            )

        os.replace(temp_name, target)
        temp_name = None
        return actual_sha256
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)


def main() -> None:
    parser = argparse.ArgumentParser(description="Download an explicitly selected MACROGUARD source file.")
    parser.add_argument("--url", required=True, help="Publisher-approved direct download URL")
    parser.add_argument("--output", required=True, help="Destination path for the raw source file")
    parser.add_argument("--sha256", help="Optional expected SHA-256 checksum")
    args = parser.parse_args()

    checksum = download_file(args.url, args.output, expected_sha256=args.sha256)
    print(f"Saved: {args.output}")
    print(f"SHA-256: {checksum}")


if __name__ == "__main__":
    main()
