# REQUIRED CONFIG
BOT_TOKEN = "7867074530:AAFp-7DUCJiW93aJmsfhWnSduj0aZfy81zo"
OWNER_ID = "2135601715"
TELEGRAM_API = "23049826"
TELEGRAM_HASH = "4a4216f089ce68a3ce2c8b9b9a6fa79a"

# SEMI-REQUIRED, WE SUGGEST TO FILL IT FROM MONGODB
DATABASE_URL = "mongodb+srv://aman:hdhub4net@cluster0.f6fbxm4.mongodb.net/?retryWrites=true&w=majority"

# OPTIONAL CONFIG
TG_PROXY = {}
USER_SESSION_STRING = ""
DOWNLOAD_DIR = "/usr/src/app/downloads/"
CMD_SUFFIX = ""
AUTHORIZED_CHATS = ""
SUDO_USERS = ""
DEFAULT_UPLOAD = "rc"
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SUBSTITUTE = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# INKYPINKY
DELETE_LINKS = False
FSUB_IDS = ""
TOKEN_TIMEOUT = 0
PAID_CHANNEL_ID = 0
PAID_CHANNEL_LINK = ""
SET_COMMANDS = True
METADATA_KEY = ""
WATERMARK_KEY = ""
LOG_CHAT_ID = 0
LEECH_FILENAME_CAPTION = ""
HYDRA_IP = ""
HYDRA_API_KEY = ""
INSTADL_API = ""

# GDrive Tools
GDRIVE_ID = ""
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# Mega credentials
MEGA_EMAIL = ""
MEGA_PASSWORD = ""

# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    },
]

# Update
UPSTREAM_REPO = "https://github.com/AeonOrg/Aeon-MLTB"
UPSTREAM_BRANCH = "main"

# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
MEDIA_GROUP = False
USER_TRANSMISSION = False
HYBRID_LEECH = False
LEECH_FILENAME_PREFIX = ""
LEECH_DUMP_CHAT = []
THUMBNAIL_LAYOUT = ""

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 80
WEB_PINCODE = False

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Heroku config for get BASE_URL automatically
HEROKU_APP_NAME = ""
HEROKU_API_KEY = ""
