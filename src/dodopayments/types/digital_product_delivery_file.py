# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DigitalProductDeliveryFile"]


class DigitalProductDeliveryFile(BaseModel):
    file_id: str

    file_name: str

    url: str
