import discord
from discord.ext import commands


class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hola soy tu primer bot")

async def setup(bot):
    await bot.add_cog(Command(bot))
