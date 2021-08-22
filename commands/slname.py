@divinity.command(aliases=["stopautoname", "stoploopname", "sautoname", "sloopname", "slname"])
async def stoplname(ctx):
    await ctx.message.delete()
    global lname
    lname = False
