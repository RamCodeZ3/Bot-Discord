import discord
from discord.ext import commands
import json
import os

SETTINGS_FILE = "data/settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4, ensure_ascii=False)

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_settings = load_settings()

    # Comandos del bot
    @commands.command()
    async def presentation(self, ctx):
        await ctx.send("Soy un bot que le gusta saludar a las personas :D")
    
    @commands.command()
    async def setwelcome(self, ctx, *, mensaje: str):
        guild_id = str(ctx.guild.id)
        if guild_id not in self.guild_settings:
            self.guild_settings[guild_id] = {}
        self.guild_settings[guild_id]["welcome"] = mensaje
        save_settings(self.guild_settings)
        await ctx.send(f"Se configuró tu mensaje de bienvenida:\n```{mensaje}```")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setgoodbye(self, ctx, *, mensaje: str):
        guild_id = str(ctx.guild.id)
        if guild_id not in self.guild_settings:
            self.guild_settings[guild_id] = {}
        self.guild_settings[guild_id]["goodbye"] = mensaje
        save_settings(self.guild_settings)
        await ctx.send(f"Se configuró tu mensaje de despedida:\n```{mensaje}```")

    # Eventos de entrada y salida
    @commands.Cog.listener()
    async def on_member_join(self, member):
        settings = load_settings()
        guild_id = str(member.guild.id)
        welcome_msg = settings.get(guild_id, {}).get("welcome", f"👋 Bienvenido {member.name} :D")
        if member.guild.system_channel:
            await member.guild.system_channel.send(welcome_msg.replace("{user}", member.mention))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        settings = load_settings()
        guild_id = str(member.guild.id)
        goodbye_msg = settings.get(guild_id, {}).get("goodbye", f"Adiós {member.name} :c")
        if member.guild.system_channel:
            await member.guild.system_channel.send(goodbye_msg.replace("{user}", member.name))

async def setup(bot):
    await bot.add_cog(Command(bot))
