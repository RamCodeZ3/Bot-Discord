import discord
from discord.ext import commands
from function_json import load_settings

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        settings = load_settings()
        guild_id = str(member.guild.id)
        welcome_msg = settings.get(guild_id, {}).get(
            "welcome",
            f"Bienvenido {member.name} :D")
        if member.guild.system_channel:
            await member.guild.system_channel.send(
                welcome_msg.replace(
                    "{user}",
                    member.mention))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        settings = load_settings()
        guild_id = str(member.guild.id)
        goodbye_msg = settings.get(guild_id, {}).get(
            "goodbye",
            f"Adiós {member.name} :c")
        
        if member.guild.system_channel:
            await member.guild.system_channel.send(
                goodbye_msg.replace(
                    "{user}",
                    member.name))

async def setup(bot):
    await bot.add_cog(Event(bot))