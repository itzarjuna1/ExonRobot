import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(os.getenv("API_ID", ))
    API_HASH = os.getenv("API_HASH", None)
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = os.getenv("TOKEN", None)
    OWNER_ID = int(os.getenv("OWNER_ID", 7651303468)
    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "cyber_github")
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "snowy_hometown")
    LOGGER_ID = int(os.getenv("LOGGER_ID", "-1003748760283"))
    MONGO_URI = os.getenv(
        "MONGO_DB_URI",
        "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority",
    )
    DB_NAME = os.getenv("DB_NAME", "ExonRobot")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = os.getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
