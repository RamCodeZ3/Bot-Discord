import discord
from discord.ext import commands


class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hola soy tu primer bot")


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name="general")
        if channel:
            await channel.send(f"{member.mention}")


    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name="general")
        if channel:
            await channel.send(f"{member.mention}")


async def setup(bot):
    await bot.add_cog(Command(bot))
