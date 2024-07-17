import discord
from discord.ext import commands, tasks

from clients import OpenDotaClient
from utils import generate_text
from env import LOOP_TIMEOUT

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

last_match_id = 1

@bot.command()
async def watch(ctx, dota_id: str):
  await check_stat.start(ctx, dota_id)
    
@tasks.loop(seconds=float(LOOP_TIMEOUT))
async def check_stat(ctx, dota_id):
  global last_match_id

  dota_client = OpenDotaClient(dota_id)
  stats = dota_client.get_last_match()
  match_id = stats["match_id"]
  account = dota_client.get_account()
  text = generate_text(stats, account)
  
  if(match_id != last_match_id):
    await ctx.send(text)
    last_match_id = match_id
