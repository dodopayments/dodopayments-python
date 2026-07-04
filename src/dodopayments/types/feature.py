# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .feature_type import FeatureType

__all__ = ["Feature"]


class Feature(BaseModel):
    """Capability conferred by a `feature_flag` grant."""

    feature_id: str
    """Identifier of the capability this grant confers."""

    feature_type: FeatureType
    """Type of capability conferred."""
