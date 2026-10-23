"""Result types shared across ngstats.

All result classes are frozen dataclasses with no dependency on the API layer.
"""

from dataclasses import dataclass
from typing import Literal

__all__ = ["Alternative", "HypothesisTestResult"]

Alternative = Literal["two-sided", "less", "greater"]
"""The alternative hypothesis, using scipy's names."""


@dataclass(frozen=True, slots=True, kw_only=True)
class HypothesisTestResult:
    """The outcome of a hypothesis test.

    Parameters
    ----------
    test_name : str
        Identifier of the test, e.g. ``"t_test"`` or ``"wilcoxon_signed_rank"``.
    stat_name : str
        Conventional symbol for the test statistic, e.g. ``"t"``, ``"W"``, ``"chi2"``.
    test_stat_value : float
        Value of the test statistic.
    df : float or tuple of float or None, optional
        Degrees of freedom. A tuple ``(numerator, denominator)`` for F tests;
        ``None`` for tests without degrees of freedom. Default is ``None``.
    p_value : float
        The p-value, in [0, 1].
    alternative : {"two-sided", "less", "greater"}
        The alternative hypothesis that was tested.
    alpha : float
        Significance level specified by the caller, in (0, 1).

    Raises
    ------
    ValueError
        If `p_value` is outside [0, 1] or `alpha` is outside (0, 1).
    """

    test_name: str
    stat_name: str
    test_stat_value: float
    df: float | tuple[float, float] | None = None
    p_value: float
    alternative: Alternative
    alpha: float

    def __post_init__(self) -> None:
        """Validate the probability fields."""
        if not 0.0 <= self.p_value <= 1.0:
            raise ValueError(f"p_value must be in [0, 1], got {self.p_value}")
        if not 0.0 < self.alpha < 1.0:
            raise ValueError(f"alpha must be in (0, 1), got {self.alpha}")

    @property
    def reject_null(self) -> bool:
        """bool: Whether the null hypothesis is rejected at `alpha`."""
        return self.p_value < self.alpha

    @property
    def interpretation(self) -> str:
        """str: Plain-language conclusion of the test."""
        if self.reject_null:
            return "Reject the null hypothesis."
        return "Fail to reject the null hypothesis."
