from dacite import from_dict

from discore.models import User


def test_serialize():
    example_user_data = {
        "id": "80351110224678912",
        "username": "Nelly",
        "discriminator": "1337",
        "avatar": "8342729096ea3675442027381ff50dfe",
        "verified": True,
        "email": "nelly@discord.com",
        "flags": 64,
        "premium_type": 1,
        "public_flags": 64,
    }

    assert from_dict(User, example_user_data)
