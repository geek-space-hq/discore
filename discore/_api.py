# type: ignore

from typing import no_type_check

from apywrapper import Apy, get

from .models import User


class DiscordApi(Apy):
    def __init__(self, bot_token: str) -> None:
        super().__init__(
            "https://discord.com/api", {"Authorization": f"Bot {bot_token}"}
        )

    @get("/users/@me")
    def get_my_user(self) -> User:
        return {}

    @get("/users/{user_id}")
    def get_user(self, user_id: str) -> User:
        return {"user_id": user_id}
