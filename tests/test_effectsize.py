"""Tests for ngstats.effectsize."""

import ngstats.effectsize


def test_import() -> None:
    """The subpackage imports and declares a public surface."""
    assert isinstance(ngstats.effectsize.__all__, list)
