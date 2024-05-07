# Cyberspace bot

##This source serves as a base for Cyberspace store bots.
##It aims to be as modular as possible, allowing adding new features with minor effort.

## Example config file
#6203838763:AAFKHxOaQilei4GnWtvyJ6NPXI03qwhuFI8
##```python
# Your Telegram bot token.
BOT_TOKEN = "7001845366:AAGfFZGLm2x3V8_bMmFZeyGEMp4IDvaeRuE"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 29277438
API_HASH = "e0d0ba98e03c8997211e4ed49aa16904"

# Chat used for logging errors.
LOG_CHAT = -1002139794836

# Chat used for logging user actions (like buy, gift, etc).
ADMIN_CHAT = -1001678203780
GRUPO_PUB = -1001678203780


# How many updates can be handled in parallel.
# Don't use high values for low-end servers.
WORKERS = 20

# Admins can access panel and add new materials to the bot.
ADMINS = [6293239703]

# Sudoers have full access to the server and can execute commands.
SUDOERS = [6293239703]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = [6107171260]

# Bote o Username do bot sem o @
# Exemplo: default
BOT_LINK = "djaboggBOT"



# Bote o Username do suporte sem o @
# Exemplo: suporte
BOT_LINK_SUPORTE = "eldjab0"
##```
