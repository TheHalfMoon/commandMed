"""Synthetic failure injection: never publish partial V5 development evidence."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
import v5_development_evidence_writer as writer


def test_publish_exact_data_then_collision_fails_without_clobber(tmp_path: Path) -> None:
    out = tmp_path / 'folder' / 'source-bound.json'
    original = b'{"status":"DEVELOPMENT_ONLY","confirmatory":false}\n'
    writer.publish_no_clobber(out, original)
    assert out.read_bytes() == original
    with pytest.raises(FileExistsError):
        writer.publish_no_clobber(out, b'FORGED')
    assert out.read_bytes() == original
    assert list(out.parent.iterdir()) == [out]


def test_existing_symlink_or_input_cannot_be_clobbered(tmp_path: Path) -> None:
    original = tmp_path / 'original.json'
    original.write_bytes(b'ORIGINAL_RESEARCH_EVIDENCE')
    alias = tmp_path / 'output.json'
    alias.symlink_to(original)
    for destination in (original, alias):
        with pytest.raises(FileExistsError):
            writer.publish_no_clobber(destination, b'FORGED')
    assert original.read_bytes() == b'ORIGINAL_RESEARCH_EVIDENCE'
    assert alias.is_symlink()
    assert set(tmp_path.iterdir()) == {original, alias}


@pytest.mark.parametrize('stage', ('partial', 'zero_byte', 'sync', 'publish'))
def test_write_failure_leaves_no_visible_evidence_or_temp_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stage: str,
) -> None:
    destination = tmp_path / 'evidence.json'
    actual_write = writer.os.write
    attempts = 0

    def half_then_io_error(fd: int, contents: bytes | memoryview) -> int:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return actual_write(fd, contents[: max(1, len(contents) // 2)])
        raise OSError('injected disk full after partial write')

    def zero_byte(_fd: int, _contents: bytes | memoryview) -> int:
        return 0

    def inject(*_args: object) -> None:
        raise OSError('injected sync or publication failure')

    with monkeypatch.context() as patcher:
        if stage == 'partial':
            patcher.setattr(writer.os, 'write', half_then_io_error)
        elif stage == 'zero_byte':
            patcher.setattr(writer.os, 'write', zero_byte)
        elif stage == 'sync':
            patcher.setattr(writer.os, 'fsync', inject)
        else:
            patcher.setattr(writer.os, 'link', inject)
        with pytest.raises(OSError):
            writer.publish_no_clobber(destination, b'{"incomplete":false}' * 10)
    assert not destination.exists()
    assert list(tmp_path.iterdir()) == []


def test_short_write_retries_correctly(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    target = tmp_path / 'full.json'
    data = b'case-first no power authority\n' * 11
    real_write = writer.os.write
    calls = 0

    def write_at_most_seven(fd: int, buf: bytes | memoryview) -> int:
        nonlocal calls
        calls += 1
        return real_write(fd, buf[:7])

    with monkeypatch.context() as patcher:
        patcher.setattr(writer.os, 'write', write_at_most_seven)
        writer.publish_no_clobber(target, data)
    assert calls > 2
    assert target.read_bytes() == data
    assert list(tmp_path.iterdir()) == [target]
