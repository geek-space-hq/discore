from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class User:
    id: str
    username: str
    discriminator: str
    bot: bool = field(default=False)
    system: bool = field(default=False)
    mfa_enabled: bool = field(default=False)
    verified: bool = field(default=False)
    premium_type: Optional[int] = None
    avatar: Optional[str] = None
    locale: Optional[str] = None
    email: Optional[str] = None
    flags: Optional[int] = None
    public_flags: Optional[int] = None
