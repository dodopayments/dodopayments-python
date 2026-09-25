# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .moderation_provenance import ModerationProvenance

__all__ = ["ModerationCategoryProvenance"]


class ModerationCategoryProvenance(BaseModel):
    """How each score in `categories` was measured."""

    child_sexual_exploitation: ModerationProvenance
    """Child sexual exploitation."""

    defamation: ModerationProvenance
    """False depiction that is likely to injure the reputation of a real person."""

    hate: ModerationProvenance
    """Demeaning people because of a protected characteristic."""

    indiscriminate_weapons: ModerationProvenance
    """Chemical, biological, radiological, nuclear or explosive weapons."""

    intellectual_property: ModerationProvenance
    """Copyright or trademark infringement."""

    living_artist_style: ModerationProvenance
    """Imitation of the signature style of a specific living artist."""

    minor_coded_language: ModerationProvenance
    """Age-coded language that suggests the subject is a minor."""

    non_consensual_intimate_imagery: ModerationProvenance
    """
    Non-consensual intimate imagery: undressing, nudifying or sexualising a real
    person.
    """

    non_violent_crimes: ModerationProvenance
    """Non-violent crimes."""

    privacy: ModerationProvenance
    """Sensitive private information about a person."""

    prompt_injection: ModerationProvenance
    """An attempt to override or manipulate the instructions of the system."""

    real_person_likeness: ModerationProvenance
    """The likeness of a real, identifiable, named person."""

    sex_related_crimes: ModerationProvenance
    """Sex-related crimes."""

    sexual_content: ModerationProvenance
    """Sexually explicit or pornographic content."""

    specialized_advice: ModerationProvenance
    """Unqualified financial, medical, legal or electoral advice."""

    suicide_and_self_harm: ModerationProvenance
    """Suicide and self-harm."""

    violent_crimes: ModerationProvenance
    """Violent crimes."""
