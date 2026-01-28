"""Interact with the Figshare API."""


import requests
from pydantic import BaseModel, ByteSize, HttpUrl

__all__ = [
    "File",
    "get_files",
]

BASE_URL = "https://api.figshare.com/v2/articles"


class File(BaseModel):
    """An object representing a file in Figshare."""

    id: int
    name: str
    size: ByteSize
    is_link_only: bool
    download_url: HttpUrl
    supplied_md5: str | None = None
    computed_md5: str | None = None
    mimetype: str | None = None


def get_files(record_id: int) -> list[File]:
    """Get files for a record."""
    url = f"{BASE_URL}/{record_id}/files"
    res = requests.get(url, timeout=5)
    res.raise_for_status()
    return [File.model_validate(f) for f in res.json()]
