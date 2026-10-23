"""ngstats: a friendlier interface to statsmodels and scipy.stats.

The public API is re-exported here. Import from ``ngstats`` (or its public
subpackages), never from the underscore-prefixed modules inside them.
"""

from ngstats import effectsize, inference, results

__all__ = [
    # subpackages
    "effectsize",
    "inference",
    "results",
]
