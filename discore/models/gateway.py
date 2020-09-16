from __future__ import annotations

from enum import IntEnum
from typing import Dict, Optional

from pydantic import BaseModel


class GatewayPayload(BaseModel):
    op: GatewayOpCode
    d: Dict
    s: Optional[int] = None
    t: Optional[str] = None


class GatewayOpCode(IntEnum):
    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    RECONNECT = 7
    REQUEST_GUILDMEMBERS = 8
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11
