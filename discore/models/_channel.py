from datetime import datetime
from enum import IntEnum
from typing import List, Optional, Union

from pydantic import BaseModel
from pydantic.fields import Field

# pylint: disable=unused-import
from ._user import User


class Channel(BaseModel):
    id: str
    type: int
    guild_id: Optional[str] = None
    position: Optional[int] = None
    permission_overwrites: Optional["Overwrite"] = None
    name: Optional[str] = None
    topic: Optional[str] = None
    nsfw: bool = Field(default=False)
    last_message_id: Optional[str] = None
    bitrate: Optional[int] = None
    user_limit: Optional[int] = None
    rate_limit_per_user: Optional[int] = None
    recipients: Optional[List["User"]] = None
    icon: Optional[str] = None
    parent_id: Optional[str] = None
    last_pin_timestamp: Optional[datetime] = None


class ChannelTypes(IntEnum):
    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEWS = 5
    GUILD_STORE = 6


class OverwriteReceiving(BaseModel):
    id: str
    type: str
    allow: int
    allow_new: str
    deny: int
    deny_new: str


class OverwriteSending(BaseModel):
    id: str
    type: str
    allow: Union[int, str]
    deny: Union[int, str]


Overwrite = Union[OverwriteReceiving, OverwriteSending]
