@divinity.command(aliases=["autoname", "loopname"])
async def lname(ctx, *, text):
    await ctx.message.delete()
    global lname
    lname = True
    while lname:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)
