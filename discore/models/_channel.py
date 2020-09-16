from datetime import datetime
from enum import IntEnum
from typing import List, Optional, Union

from pydantic import BaseModel
from pydantic.fields import Field

# pylint: disable=unused-import
from ._guild import GuildMember, Role
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


class Message(BaseModel):
    id: str
    channel_id: str
    aurhor: "User"
    content: str
    timestamp: datetime
    tts: bool
    mention_everyone: bool
    mentions: List["UserMentioned"]
    mention_roles: List["Role"]
    attachments: List["Attachment"]
    embeds: List["Embed"]
    pinned: bool
    type: "MessageType"
    guild_id: Optional[str] = None
    member: Optional["GuildMember"] = None
    mention_channels: Optional[List["ChannelMention"]] = None
    reactions: Optional[List["Reaction"]] = None
    nonce: Optional[Union[int, str]] = None
    webhook_id: Optional[str] = None
    activity: Optional["MessageActivity"] = None
    application: Optional["MessageApplication"] = None
    message_reference: Optional["MessageReference"] = None
    flags: Optional[int] = None


class UserMentioned(User):
    member: "GuildMember"


class MessageType(IntEnum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    GUILD_MEMBER_JOIN = 7
    USER_PREMIUM_GUILD_SUBSCRIPTION = 8
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_1 = 9
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_2 = 10
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15


class MessageActivity(BaseModel):
    type: int
    party_id: Optional[str] = None


class MessageApplication(BaseModel):
    id: str
    description: str
    name: str
    cover_image: Optional[str] = None
    icon: Optional[str] = None


class MessageReference(BaseModel):
    channel_id: str
    message_id: Optional[str] = None
    guild_id: Optional[str] = None


class MessageActivityType(IntEnum):
    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5


class MessageFlag(IntEnum):
    CROSSPOSTED = 1 << 0
    IS_CROSSPOST = 1 << 1
    SUPPRESS_EMBEDS = 1 << 2
    SOURCE_MESSAGE_DELETED = 1 << 3
    URGENT = 1 << 4


class FollowedChannel(BaseModel):
    channel_id: str
    webhook_id: str


class Reaction:
    count: int
    me: bool
    emoji: "Emoji"


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
