# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ModerationCategoryScores"]


class ModerationCategoryScores(BaseModel):
    """The probability, from 0 to 1, that the screen falls in each category."""

    child_sexual_exploitation: float
    """Child sexual exploitation."""

    defamation: float
    """False depiction that is likely to injure the reputation of a real person."""

    hate: float
    """Demeaning people because of a protected characteristic."""

    indiscriminate_weapons: float
    """Chemical, biological, radiological, nuclear or explosive weapons."""

    intellectual_property: float
    """Copyright or trademark infringement."""

    living_artist_style: float
    """Imitation of the signature style of a specific living artist."""

    minor_coded_language: float
    """Age-coded language that suggests the subject is a minor."""

    non_consensual_intimate_imagery: float
    """
    Non-consensual intimate imagery: undressing, nudifying or sexualising a real
    person.
    """

    non_violent_crimes: float
    """Non-violent crimes."""

    privacy: float
    """Sensitive private information about a person."""

    prompt_injection: float
    """An attempt to override or manipulate the instructions of the system."""

    real_person_likeness: float
    """The likeness of a real, identifiable, named person."""

    sex_related_crimes: float
    """Sex-related crimes."""

    sexual_content: float
    """Sexually explicit or pornographic content."""

    specialized_advice: float
    """Unqualified financial, medical, legal or electoral advice."""

    suicide_and_self_harm: float
    """Suicide and self-harm."""

    violent_crimes: float
    """Violent crimes."""
