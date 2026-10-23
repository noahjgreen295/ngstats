"""Tests for ngstats.results."""

import math

import pytest

import ngstats.results
from ngstats.results import HypothesisTestResult


def make_result(*, p_value: float = 0.03, alpha: float = 0.05) -> HypothesisTestResult:
    """Build a valid result, overriding the probability fields."""
    return HypothesisTestResult(
        test_name="t_test",
        stat_name="t",
        test_stat_value=2.1,
        df=10.0,
        p_value=p_value,
        alternative="two-sided",
        alpha=alpha,
    )


def test_import() -> None:
    """The module imports and declares a public surface."""
    assert isinstance(ngstats.results.__all__, list)


@pytest.mark.parametrize("p_value", [0.0, 0.5, 1.0])
def test_p_value_in_range_is_accepted(p_value: float) -> None:
    """p_value anywhere in the closed interval [0, 1] is valid."""
    assert make_result(p_value=p_value).p_value == p_value


@pytest.mark.parametrize("p_value", [-0.01, 1.01, -math.inf, math.inf, math.nan])
def test_p_value_out_of_range_raises(p_value: float) -> None:
    """p_value outside [0, 1] raises ValueError."""
    with pytest.raises(ValueError, match="p_value"):
        make_result(p_value=p_value)


@pytest.mark.parametrize("alpha", [1e-9, 0.05, 1 - 1e-9])
def test_alpha_in_range_is_accepted(alpha: float) -> None:
    """Any alpha in the open interval (0, 1) is valid."""
    assert make_result(alpha=alpha).alpha == alpha


@pytest.mark.parametrize("alpha", [0.0, 1.0, -0.05, 1.5, math.inf, math.nan])
def test_alpha_out_of_range_raises(alpha: float) -> None:
    """An alpha outside (0, 1), including the endpoints, raises ValueError."""
    with pytest.raises(ValueError, match="alpha"):
        make_result(alpha=alpha)
