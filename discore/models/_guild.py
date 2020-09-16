from __future__ import annotations

from datetime import datetime
from enum import Enum, IntEnum
from typing import TYPE_CHECKING, List, Optional

from pydantic import BaseModel
from pydantic.fields import Field

if TYPE_CHECKING:
    from ._channel import Channel
    from ._emoji import Emoji
    from ._user import User
    from ._voice import VoiceState


class Guild(BaseModel):
    id: str
    name: str
    owner_id: str
    region: str
    afk_timeout: int
    verification_level: int
    default_message_notifications: int
    explicit_content_filter: int
    roles: List["Role"]
    emojis: List["Emoji"]
    features: List["GuildFeature"]
    mfa_level: int
    system_channel_flags: int
    premium_tier: int
    preferred_locale: str
    public_updates_channel_id: Optional[str] = None
    max_video_channel_users: Optional[int] = None
    approximate_member_count: Optional[int] = None
    approximate_presence_count: Optional[int] = None
    rules_channel_id: Optional[str] = None
    joined_at: Optional[datetime] = None
    large: bool = Field(default=False)
    unavailable: bool = Field(default=False)
    member_count: Optional[int] = None
    voice_states: Optional[List["VoiceState"]] = None
    members: Optional[List["GuildMember"]] = None
    channels: Optional[List["Channel"]] = None
    presences: Optional[List["PresenceUpdate"]] = None
    max_presences: Optional[int] = None
    max_members: Optional[int] = None
    vanity_url_code: Optional[str] = None
    description: Optional[str] = None
    banner: Optional[str] = None
    application_id: Optional[str] = None
    icon: Optional[str] = None
    splash: Optional[str] = None
    discovery_splash: Optional[str] = None
    afk_channel_id: Optional[str] = None
    owner: bool = Field(default=False)
    permissions: Optional[int] = None
    permissions_new: Optional[str] = None
    embed_enabled: bool = Field(default=False)
    embed_channel_id: Optional[str] = None
    widget_channel_id: Optional[str] = None
    system_channel_id: Optional[str] = None


class MessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class ContentFilterLevel(IntEnum):
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class VerificationLevel(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class PremiumTier(IntEnum):
    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class SystemChannelFlag(IntEnum):
    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1


class GuildFeature(Enum):
    INVITE_SPLASH = "INVITE_SPLASH"
    VIP_REGIONS = "VIP_REGIONS"
    VANITY_URL = "VANITY_URL"
    VERIFIED = "VERIFIED"
    PARTNERED = "PARTNERED"
    PUBLIC = "PUBLIC"
    COMMERCE = "COMMERCE"
    NEWS = "NEWS"
    DISCOVERABLE = "DISCOVERABLE"
    FEATURABLE = "FEATURABLE"
    ANIMATED_ICON = "ANIMATED_ICON"
    BANNER = "BANNER"
    PUBLIC_DISABLED = "PUBLIC_DISABLED"
    WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"


class Role(BaseModel):
    id: str
    name: str
    color: int
    hoist: bool
    position: int
    permission: int
    permission_new: str
    managed: bool
    mentionable: bool


class GuildPreview(BaseModel):
    id: str
    name: str
    emojis: List["Emoji"]
    features: List["GuildFeature"]
    approximate_member_count: int
    approximate_presence_count: int
    icon: Optional[str] = None
    splash: Optional[str] = None
    discovery_splash: Optional[str] = None
    description: Optional[str] = None


class GuildWidget(BaseModel):
    enabaled: bool
    channel_id: str


class GuildMember(BaseModel):
    roles: List[str]
    joined_at: datetime
    deaf: bool
    mute: bool
    user: Optional["User"] = None
    nick: Optional[str] = None
    premium_since: Optional[datetime] = None


class Integration(BaseModel):
    id: str
    name: str
    type: str
    enabled: bool
    syncing: bool
    role_id: str
    expire_behavior: "ExipireBehaviorType"
    expire_grace_period: int
    user: "User"
    account: "IntegrationAccount"
    synced_at: datetime
    enable_emoticons: Optional[bool] = None


class ExipireBehaviorType(IntEnum):
    REMOVE_ROLE = 0
    KICK = 1


class IntegrationAccount(BaseModel):
    id: str
    name: str


class Ban(BaseModel):
    user: "User"
    reason: Optional[str] = None
