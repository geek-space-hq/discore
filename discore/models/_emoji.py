from typing import List, Optional

# pylint: disable=unused-import
from ._guild import Role
from ._user import User


class Emoji:
    id: Optional[str] = None
    name: Optional[str] = None
    roles: Optional[List["Role"]] = None
    user: Optional["User"] = None
    require_colons: Optional[bool] = None
    managed: Optional[bool] = None
    animated: Optional[bool] = None
    available: Optional[bool] = None
