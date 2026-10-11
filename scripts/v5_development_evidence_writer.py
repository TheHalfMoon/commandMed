"""Publish completed *development-only* evidence bytes without partial filenames.

This helper never rewrites existing research evidence or makes scientific claims.
"""
from __future__ import annotations

import os
from pathlib import Path
import tempfile


def publish_no_clobber(path: Path, contents: bytes) -> None:
    """Write+sync privately, then atomically add the completed destination name.

    The temporary file and destination must reside on the same filesystem.
    A hard link refuses an existing file or symlink, even if another writer
    races publication. No replace/rename fallback is allowed. Directory fsync
    and total power-loss durability are explicitly not guaranteed.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temp = Path(name)
    try:
        try:
            remainder = memoryview(contents)
            while remainder:
                size = os.write(fd, remainder)
                if size <= 0:
                    raise OSError("incomplete evidence write")
                remainder = remainder[size:]
            os.fsync(fd)
        finally:
            os.close(fd)
        # Link rather than rename/replace so a concurrently created destination
        # cannot be clobbered after the first existence check.
        os.link(temp, path)
    finally:
        temp.unlink(missing_ok=True)
