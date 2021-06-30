from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class Tagging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @commands.command()
    async def tag(self, ctx, tag: str):
        clean_name = ctx.channel.name.split("｜", maxsplit=1)[-1]
        await ctx.channel.edit(name=f"{tag}｜{clean_name}")
        await ctx.message.add_reaction("\u2705")


def setup(bot):
    bot.add_cog(Tagging(bot))
