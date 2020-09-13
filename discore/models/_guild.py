from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional

from ._emoji import Emoji


@dataclass
class Guild:
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
    features: List[str]
    mfa_level: int
    system_channel_flags: int
    premium_tier: int
    preferred_locale: str
    public_updates_channel_id: Optional[str] = None
    max_video_channel_users: Optional[int] = None
    approximate_member_count: Optional[int] = None
    approximate_presence_count: Optional[int] = None
    rules_channel_id: Optional[str] = None
    joined_at: Optional[str] = None
    large: bool = field(default=False)
    unavailable: bool = field(default=False)
    member_count: Optional[int] = None
    voice_states: Optional[List["VoiceState"]] = None
    members: Optional[List["GuildMember"]] = None
    channels: Optional[List["Channel"]] = None
    presences: Optional[List["PresenceUpdateSimplified"]] = None
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
    owner: bool = field(default=False)
    permissions: Optional[int] = None
    permissions_new: Optional[str] = None
    embed_enabled: bool = field(default=False)
    embed_channel_id: Optional[str] = None
    widget_channel_id: Optional[str] = None
    system_channel_id: Optional[str] = None


@dataclass
class Role:
    id: str
    name: str
    color: int
    hoist: bool
    position: int
    permission: int
    permission_new: str
    managed: bool
    mentionable: bool
