from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID","11174745"))
API_HASH = getenv("API_HASH","364a3329a7dc1fa55f8d59229e62b65e")
BOT_TOKEN = getenv("BOT_TOKEN","5180441164:AAFo3gGSjouNFECJ_Ie931zydnTGjImiMBI")
SESSION_NAME = getenv("SESSION_NAME", "BABURdPT6QoKvarUId_SBMBh27y_CZpx8qPI6BjV_1GVxtENpaBRqoAYGyAAqymJReBG0ZJMQq4GvewRcLqEVm1BS14hCoJoJvl2gYvEsJgLr-76zm90AnwB_x357LNRRWBdOveu_2Gf0__2jvQW9ioPNnMg9E2PTsIucVkyzhhcZAJKn1c5ADs6qpHEW9Ce4QTFWFSttBRRl7Be-3EyXjK9AImcS7Fj4ethbYgd-AkwRX5RHu4MGZduIC6bWemW2uW3r026si9zn15x4lNmxSTc0ptKA-DtYVNJ3XVRa_Sauy-WzY6Ok39kWVs71ZcmcL-PALBHOtryvXOnn1_RgBbwAAAAAUl3DIQA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME","G_W_P")
ALIVE_NAME = getenv("ALIVE_NAME","Song_Nova")
BOT_USERNAME = getenv("BOT_USERNAME","TsNoBot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/So-Nova/iMusic")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GhNova")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TmNova")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ت ا ش و ك ر غ ب ف م / ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID","5125194988").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5527506052").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c6cc20e377eb6c0f33b07.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/c6cc20e377eb6c0f33b07.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c6cc20e377eb6c0f33b07.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/c6cc20e377eb6c0f33b07.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c6cc20e377eb6c0f33b07.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c6cc20e377eb6c0f33b07.jpg")
