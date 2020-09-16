from __future__ import annotations

from enum import IntEnum
from typing import List, Optional

from pydantic import BaseModel
from pydantic.fields import Field

from ._guild import GuildMember, Integration


class User(BaseModel):
    id: str
    username: str
    discriminator: str
    bot: bool = Field(default=False)
    system: bool = Field(default=False)
    mfa_enabled: bool = Field(default=False)
    verified: bool = Field(default=False)
    avatar: Optional[str] = None
    locale: Optional[str] = None
    email: Optional[str] = None
    flags: Optional[UserFlag] = None
    premium_type: Optional[int] = None
    public_flags: Optional[UserFlag] = None


class UserMentioned(User):
    member: GuildMember


class UserFlag(IntEnum):
    Null = 0
    DiscordEmployee = 1 << 0
    DiscordPartner = 1 << 1
    HypeSquadEvents = 1 << 2
    BugHunterLevel1 = 1 << 3
    HouseBravery = 1 << 6
    HouseBrilliance = 1 << 7
    HouseBalance = 1 << 8
    EarlySupporter = 1 << 9
    TeamUser = 1 << 10
    System = 1 << 12
    BugHunterLevel2 = 1 << 14
    VerifiedBot = 1 << 16
    VerifiedBotDeveloper = 1 << 17


class PremiumType(IntEnum):
    Null = 0
    NitroClassic = 1
    Nitro = 2


class Connection:
    id: str
    name: str
    type: str
    verified: bool
    firend_sync: bool
    show_activity: bool
    visibility: VisibilityType
    revoked: Optional[bool] = None
    integrations: Optional[List[Integration]] = None


class VisibilityType(IntEnum):
    Null = 0
    Everyone = 1


User.update_forward_refs()
