from __future__ import annotations

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

from ._user import User


class Webhook(BaseModel):
    id: str
    type: WebhookType
    channel_id: str
    guild_id: Optional[str] = None
    user: Optional[User] = None
    name: Optional[str] = None
    avater: Optional[str] = None
    token: Optional[str] = None


class WebhookType(IntEnum):
    INCOMING = 1
    CHANNEL_FOLLOWER = 2
