@divinity.command(aliases=["pornhubcomment", "phc"])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.divinitySession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"divinity_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])
