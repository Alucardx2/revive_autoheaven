import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '16913514') )
API_HASH = environ.get('API_HASH', '9996dfffaa4a745d8a99e0dc73f570a9')
BOT_TOKEN = environ.get('BOT_TOKEN', '5264501642:AAEunzhg-TXEFw4h4iHfqojYZZRfHJGJaHY')

# Bot settings
PORT = environ.get("PORT", "8080")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/c94418669129fc55f8575.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/76b38816c46209b495d47.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/ca99c6c62072f860ad3d1.jpg")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/3bed35ee47a26f935a170.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '890230886 1154404230 1921088773 1612173220 1120465309 1268492137 930859384 1994336709').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001444805977').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001534801897')
auth_grp = environ.get('AUTH_GROUPS', '-1001573188040')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
FILDLT_CNL = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('FILDLT_CNL', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://saurabh:saurabh@cluster0.wjhqcxl.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+wpYpIGZM_tg3ZjA1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+c7TFIJtvDCpiYzU1')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Heavens Chat')
MSG_ALRT = environ.get('MSG_ALRT', 'Share and Support Us')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
HOW_DWLD_LINK = environ.get('HOW_DWLD_LINK', 'https://t.me/HeavenForYouAll/7878')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001681090295'))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', 0))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "[{file_name}](https://t.me/HeavenRequest)\n\n<b>•────•────────•────•\n📌 ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/HeavenRequest)\n🎬 ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/HeavenForYouAll)\n•────•────────•────•\n\n©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ʜᴇᴀᴠᴇɴ ʀᴇQᴜᴇꜱᴛ](https://t.me/HeavenRequest)</b>")

BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>{mention}'s Qᴜᴇʀʏ ☞ <code>{query}</code>\n\n<b>🏷 Tɪᴛʟᴇ</b> : <a href={url}>{title}</a>\n\n🌟 Rᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10\n💀 Rᴇʟᴇᴀsᴇ :  <b>{release_date}</b> <b>{countries}</b>\n\n🎭 Gᴇɴʀᴇs : <b>#{genres}</b></b>\n\n<b>🔅 Pᴏᴡᴇʀᴇᴅ Bʏ : {message.chat.title}</b>")
KD_IMDB_TEMPLATE = environ.get("KD_IMDB_TEMPLATE", "<b><b>🏷 Tɪᴛʟᴇ</b> : <a href={url}>{title}</a>\n\n🌟 Rᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10\n💀 Rᴇʟᴇᴀsᴇ :  <b>{release_date}</b> <b>{countries}</b>\n\n🎭 Gᴇɴʀᴇs : <b>{genres}</b></b>\n\n<b>📖 Sᴛᴏʀʏ Lɪɴᴇ :</b> <code>{plot}</code>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Auto Delete , Filter & Auto Filter
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
MAUTO_DELETE = is_enabled((environ.get('MAUTO_DELETE', "True")), True)

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
SPL_DELETE_TIME = int(environ.get('SPL_DELETE_TIME', 15))

# Url Shortner
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'tnlink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '75da926e3f248de287cb0a770ea77048012fa926')

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
