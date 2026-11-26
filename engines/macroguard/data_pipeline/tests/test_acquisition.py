import hashlib

import pytest

from engines.macroguard.data_pipeline.acquisition import download_file


def test_download_uses_checksum_and_writes_file(tmp_path, monkeypatch):
    content = b"date,value\n2024-01-01,0.2\n"
    expected = hashlib.sha256(content).hexdigest()

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self, size=-1):
            nonlocal content
            chunk, content = content[:size], content[size:]
            return chunk

    monkeypatch.setattr(
        "engines.macroguard.data_pipeline.acquisition.urlopen",
        lambda *args, **kwargs: FakeResponse(),
    )

    destination = tmp_path / "raw.csv"
    actual = download_file("https://example.invalid/data.csv", destination, expected_sha256=expected)

    assert actual == expected
    assert destination.read_bytes() == b"date,value\n2024-01-01,0.2\n"


def test_checksum_mismatch_does_not_replace_destination(tmp_path, monkeypatch):
    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self, size=-1):
            return b"bad"

    monkeypatch.setattr(
        "engines.macroguard.data_pipeline.acquisition.urlopen",
        lambda *args, **kwargs: FakeResponse(),
    )
    destination = tmp_path / "raw.csv"
    destination.write_text("keep")

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        download_file("https://example.invalid/data.csv", destination, expected_sha256="0" * 64)

    assert destination.read_text() == "keep"
