#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5366068176:AAHdTvse2qikV-EbPshjIj9VaypO9E3yA6A")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "9844066"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCWNWIAKrD5-x1C5_Aa3tlG_gkiFbXiXN22VP6Hi5rm8NZMkoSQtP1H-Q4OOZW98b1niJ4LnDgJy_z5K85kjgcrnYrZX5JGNTAGyVcLQUEPirCIuQjIdgbdWOxVzthfjAab9NN3hHdD3v6480iwvhbeXDWwPidoD36R3lEgmRXxBJp2gTyy4Yx0TaFYW7CSHamvQIhGJTrMiwsYu1YwBdgsNk5aiO8cCgJOUgsuLuBVg8i2l6qXGeLEIpRH23FoKIPJCX_CRX3dmTimbOLg9LAtyemU8cCstpOQvwlyJtm5kZLb3cJEk_WNiVVuxItHmI3WYrLDNsvD1kDrbWyiSlYIGvbxOwAAAABphwJ4AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://clone:computer90@cluster0.jff6fof.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
