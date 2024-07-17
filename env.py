import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
LOOP_TIMEOUT = os.getenv('LOOP_TIMEOUT')
SERVER_ID = os.getenv('SERVER_ID')
