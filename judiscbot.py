import discord
from discord.ext import commands
from weather_api import fetch_weather

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
token = 'MTM0MjAzMTQ1NzA5MDE0MjIxOA.GVU7Uo.ntqzxYDNASKvGltYnsKseXPbiynLiH7sDBnB18'

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        await bot.tree.sync()  # Sync slash commands
        print("all good!")
    except Exception as e:
        print(f"An error occurred while syncing commands: {e}")


@bot.tree.command(name="weather", description="Fetches the weather details for the specified city.")
async def hello(interaction: discord.Interaction, city: str):
    weather_data = fetch_weather(city)
    await interaction.response.send_message(f"{fetch_weather(city)} ")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$is nono ugly'):
        await message.channel.send('yes!')


bot.run(token)