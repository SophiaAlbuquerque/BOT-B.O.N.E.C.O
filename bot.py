import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

xp = {}

jogos = [
    "Stardew Valley", "Terraria", "Overcooked 2"
]

def get_rank(xp_total):
    if xp_total >= 500: return "Lenda"
    if xp_total >= 300: return "Veterano"
    if xp_total >= 100: return "Aventureiro"
    return "Camponês"

@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

@bot.command()
async def jogo(ctx):
    escolha = random.choice(jogos)

    xp[ctx.author.id] = xp.get(ctx.author.id, 0) + 20
    user_xp = xp[ctx.author.id]

    await ctx.send(
        f"🎮 Hoje: {escolha}\nXP: {user_xp} | Rank: {get_rank(user_xp)}"
    )

@bot.command()
async def nivel(ctx):
    user_xp = xp.get(ctx.author.id, 0)
    await ctx.send(
        f"{ctx.author.mention} XP: {user_xp} | Rank: {get_rank(user_xp)}"
    )

@bot.command(name='hoje', aliases=['hoje_tem'])
async def hoje(ctx):
    mensagens = [
        "🔥 @everyone o caos começou!",
        "💀 @everyone vocês foram convocados!",
        "🍺 @everyone hora da bagunça!"
    ]

    await ctx.send(random.choice(mensagens))

bot.run(TOKEN)