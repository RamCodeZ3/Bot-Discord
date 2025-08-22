import discord
from discord.ext import commands


class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_join_data = {}

    # Comandos del bot
    @commands.command()
    async def presentation(self, ctx):
        await ctx.send("Saludo soy un que le gusta saludar a las personas :D")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setwelcome(self, ctx, *, mensaje: str):
        if ctx.guild.id not in self.guild_settings:
            self.guild_settings[ctx.guild.id] = {}
        self.guild_settigs[ctx.guild.id]["welcome"] = mensaje
        ctx.send(f"Se configuro tu Mensaje de bienveninda:\n{mensaje}")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setgoodbye(self, ctx, *, mensaje: str):
        if ctx.guild.id not in self.guild_settings:
            self.guild_settings[ctx.guild.id] = {}
        self.guild_settigs[ctx.guild.id]["goodbye"] = mensaje
        ctx.send(f"Se configuro tu Mensaje de despedida:\n{mensaje}")


    # Eventos de entrada y salida
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name="general")
        if channel:
            await channel.send(f"Bievenido {member.mention} :D")


    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name="general")
        if channel:
            await channel.send(f"Adios {member.mention} :c")


async def setup(bot):
    await bot.add_cog(Command(bot))
