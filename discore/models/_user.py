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
    premium_type: Optional[int] = None
    avatar: Optional[str] = None
    locale: Optional[str] = None
    email: Optional[str] = None
    flags: Optional[int] = None
    public_flags: Optional[int] = None
