import discord
from discord.ext import commands
from discord import app_commands
from function_json import (
    load_settings,
    save_settings
)


class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild_settings = load_settings()

    @app_commands.command(
    name="presentation",
    description="Presentacion del bot"
    )
    async def presentation(self, interaction: discord.Interaction):
        await interaction.channel.send("Soy un bot que le gusta saludar a las personas :D")
    
    
    @app_commands.command(
    name="setwelcome",
    description="Comando para configurar el mensaje de entrada"
    )
    async def setwelcome(self, interaction: discord.Interaction, *, mensaje: str):
        guild_id = str(interaction.guild.id)
        if guild_id not in self.guild_settings:
            self.guild_settings[guild_id] = {}
        self.guild_settings[guild_id]["welcome"] = mensaje
        save_settings(self.guild_settings)
        await interaction.channel.send(f"Se configuró tu mensaje de bienvenida:\n```{mensaje}```")
    
    @app_commands.command(
    name="setgooodbye",
    description="Comando para configurar el mensaje de salida"
    )
    @commands.has_permissions(administrator=True)
    async def setgoodbye(self, interaction: discord.Interaction, *, mensaje: str):
        guild_id = str(interaction.guild.id)
        if guild_id not in self.guild_settings:
            self.guild_settings[guild_id] = {}
        self.guild_settings[guild_id]["goodbye"] = mensaje
        save_settings(self.guild_settings)
        await interaction.channel.send(f"Se configuró tu mensaje de despedida:\n```{mensaje}```")

async def setup(bot):
    await bot.add_cog(Command(bot))
