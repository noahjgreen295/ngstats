"""Tests for ngstats.inference."""

import ngstats.inference


def test_import() -> None:
    """The subpackage imports and declares a public surface."""
    assert isinstance(ngstats.inference.__all__, list)
