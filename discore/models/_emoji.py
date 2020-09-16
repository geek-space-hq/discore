from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from ._user import User


class Emoji(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    roles: Optional[List[str]] = None
    user: Optional[User] = None
    require_colons: Optional[bool] = None
    managed: Optional[bool] = None
    animated: Optional[bool] = None
    available: Optional[bool] = None


Emoji.update_forward_refs()
