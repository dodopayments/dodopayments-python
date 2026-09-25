# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ModerationCategory"]

ModerationCategory: TypeAlias = Literal[
    "violent_crimes",
    "sex_related_crimes",
    "child_sexual_exploitation",
    "suicide_and_self_harm",
    "indiscriminate_weapons",
    "intellectual_property",
    "defamation",
    "non_violent_crimes",
    "hate",
    "privacy",
    "specialized_advice",
    "sexual_content",
    "non_consensual_intimate_imagery",
    "minor_coded_language",
    "real_person_likeness",
    "living_artist_style",
    "prompt_injection",
]
