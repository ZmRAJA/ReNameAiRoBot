from .core.get_config import get_var
from .core.handlers import add_handlers
from .Rename_Aibot import RenameAibot
from . maneuvers.ExecutorManager import ExecutorManager
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

# TODO Add a alert for an extra space recorded

if __name__ == "__main__":

    rbot = RenameAibot("RenameAibot", get_var("API_ID"), get_var("API_HASH"), 
                         bot_token=get_var("BOT_TOKEN"), workers=200)
    excm = ExecutorManager()
    add_handlers(rbot)
    rbot.run()
