from typing import Optional

from pydantic import BaseModel

# pylint: disable=unused-import
from ._guild import GuildMember


class VoiceState(BaseModel):
    user_id: str
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_video: bool
    suppress: bool
    guild_id: Optional[str] = None
    channel_id: Optional[str] = None
    member: Optional["GuildMember"] = None
    self_stream: Optional[bool] = None


class VoiceRegion(BaseModel):
    id: str
    name: str
    vip: bool
    optimal: bool
    deprecated: bool
    custom: bool
