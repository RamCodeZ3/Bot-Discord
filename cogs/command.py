import discord
from discord.ext import commands
from discord import app_commands
from src.function_json import (
    load_settings,
    save_settings
)

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

async def setup(bot):
    await bot.add_cog(Command(bot))
