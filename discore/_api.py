from typing import no_type_check

from apywrapper import Apy, get

from .models import User


class DiscordApi(Apy):
    def __init__(self, bot_token: str):
        super().__init__(
            "https://discord.com/api", {"Authorization": f"Bot {bot_token}"}
        )

    @get("/users/{user_id}")
    def get_user(self, user_id: str) -> User:
        return {"user_id": user_id}  # type: ignore
