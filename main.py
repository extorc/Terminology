from discord.ext import commands
from replit import db

bot = commands.Bot(command_prefix = "$")
termy = {}
db["terminology"] = {}

@bot.command()
async def add(ctx, *,added_termy):
	
	valid = False
	for s in added_termy:
		if s == ":":
			valid = True
			break
		else:
			valid = False
	if valid:
		termy_buffer = added_termy.split(":")
		print(termy_buffer)
		termy[termy_buffer[0]] = termy_buffer[1]
		db["terminology"] = termy
		await ctx.send("Added the Terminology : "+ added_termy[:10]+ "....")
	else:
		await ctx.send("Not a valid Terminology")


@bot.command()
async def get(ctx, query):
	await ctx.send(db["terminology"][query])

@bot.event
async def on_ready():
	print("We have logged in as {0.user}".format(bot))

bot.run("ODA1ODAyMDMwODM2MjE5OTA0.YBgLnw.nmRPs3LfhXMxEm3sImcyyUVZBdM")