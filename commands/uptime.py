@divinity.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.utcnow()
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "{d} days, {h} hours, {m} minutes, and {s} seconds."
    else:
        time_format = "{h} hours, {m} minutes, and {s} seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)