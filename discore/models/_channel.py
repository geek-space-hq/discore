from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Channel:
    id: str
    type: int
    guild_id: Optional[str] = None
