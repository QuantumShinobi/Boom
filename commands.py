async def register(ctx):
    username = ctx.message.author


async def remove(ctx):
    await ctx.send(f"{ctx.message.author.mention}, okay we are removing you")


async def tier(ctx):
    await ctx.send(f"{ctx.message.author.mention}, Your tier is one")


# @client.event
async def on_message_edit(before, after):
    await before.channel.send(f"{before.author.mention} edited a message from {before.content} to {after.content}")

# @client.event


async def on_message_delete(message):
    await message.channel.send(f"{message.author.mention} you deleted a message:\n  {message.content}")
