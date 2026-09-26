# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .moderation_category import ModerationCategory
from .moderation_decision import ModerationDecision
from .moderation_category_scores import ModerationCategoryScores
from .moderation_category_provenance import ModerationCategoryProvenance

__all__ = ["ModerationScreenResponse"]


class ModerationScreenResponse(BaseModel):
    """The verdict of one screen."""

    categories: ModerationCategoryScores
    """The probability, from 0 to 1, that the screen falls in each category."""

    compound_triggered: bool
    """
    True when real-person likeness and sexual content together crossed their
    combined threshold, the pattern of a sexual deepfake.
    """

    decision: ModerationDecision
    """The verdict.

    `allow` means the content passed. `deny` means block the content. `flag` means
    apply your own judgement. It is not a soft deny.
    """

    latency_ms: int
    """The time the screen took, in milliseconds."""

    normalized_applied: bool
    """
    True when the text was also screened in a normalized form, with obfuscation such
    as invisible or look-alike characters removed.
    """

    notes: List[str]
    """Human-readable reasons for the decision.

    The wording can change, so do not parse it.
    """

    passes: int
    """The number of yes/no questions the model answered for this screen."""

    provenance: ModerationCategoryProvenance
    """How each score in `categories` was measured."""

    request_id: Optional[str] = None
    """The `request_id` you sent, or null."""

    triggered: List[ModerationCategory]
    """The categories whose score crossed the threshold of the category.

    It can be empty on a `flag` from the general check. `notes` then gives the
    reason.
    """
