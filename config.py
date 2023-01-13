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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCWNWIAHnnxOlduK79apkgnhb9P_FA3fNcMNOCiBOfQg3SwMIeJFvSqZXsIGoy0yYZdSSbNRvSIshpoWAtBi44N4sI34OAP63QBgReFsx-5ftKIEg_MHQ1kN9HN1U_KwsBwgpSXZeoTNqXMvZc24_0kJZpHcUc1pH4Lbuzav4G5X0dLuj17VZVdGTUv9D_XnCQh0slE_76huGDqg-XRa2H-LyhWgvFNOinO1GZRn-O4zA0OZqLV_Qnrn6-FaaH1rnKFy6uqNIWo47XHKhLXnX6KYgZDntjnWYCW49oFPLfIJg6bbNrCcXA0fUSRngh0OseAZJ1E-IUjSIiLf3vagvtVJ5U8cQAAAABphwJ4AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
