from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from ._guild import Role
from ._user import User


@dataclass
class Emoji:
    id: Optional[str] = None
    name: Optional[str] = None
    roles: Optional[List["Role"]] = None
    user: Optional["User"] = None
    require_colons: bool = field(default=False)
    managed: bool = field(default=False)
    animated: bool = field(default=False)
    available: bool = field(default=False)
