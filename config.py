from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class setting():
    bot_token: str


def get_setting():
    return setting(bot_token=os.getenv("BOT_TOKEN"))