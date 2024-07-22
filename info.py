import os
# Bot information
API_ID = os.getenv('API_ID', "23990433")
API_HASH = os.getenv('API_HASH', "e6c4b6ee1933711bc4da9d7d17e1eb20")
BOT_TOKEN = os.getenv('BOT_TOKEN', "6857162781:AAEZ3C2VwSM8MaAlQAeIdiqdwfxjpmLPH3U")

# stream vars
PORT = int(os.getenv('PORT', '5050'))
BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001870015374'))#Log Channel
URL = os.getenv("URL", "https://files-suhy.onrender.com") #App URL not MongoDB URL
