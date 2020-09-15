from enum import IntEnum
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field


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
    flags: Optional["UserFlag"] = None
    premium_type: Optional[int] = None
    public_flags: Optional["UserFlag"] = None


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
