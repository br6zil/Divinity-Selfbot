@divinity.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))
