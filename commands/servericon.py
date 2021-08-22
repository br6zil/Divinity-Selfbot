@divinity.command(aliases=['svico', 'guildicon'])
async def servericon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=f"{ctx.guild.name} - Divinity Selfbot")
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)
