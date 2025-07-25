import discord
from discord.ext import tasks, commands
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

last_data = None
posted_message = None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    post_stock_data.start()

@tasks.loop(seconds=10)
async def post_stock_data():
    global last_data, posted_message
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found.")
        return

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("https://gagstock.gleeze.com/grow-a-garden") as resp:
                if resp.status != 200:
                    print(f"API returned status code {resp.status}")
                    return

                full_data = await resp.json()
                print("Received data:", full_data)  

                data = full_data.get("data")
                if not data or data == last_data:
                    return
                last_data = data

                embed = discord.Embed(
                    title="🌱 Grow A Garden Live Stock",
                    description=f"🕒 Updated: <t:{int(discord.utils.parse_time(full_data['updated_at']).timestamp())}:R>",
                    color=discord.Color.green()
                )

                def format_items(obj):
                    return "\n".join(f"{item['emoji']} {item['name']}: {item['quantity']}" for item in obj.get("items", [])) if obj else "N/A"

                embed.add_field(
                    name="🪴 Seeds",
                    value=format_items(data.get("seed")),
                    inline=False
                )
                embed.add_field(
                    name="⚙️ Gear",
                    value=format_items(data.get("gear")),
                    inline=False
                )
                embed.add_field(
                    name="🥚 Eggs",
                    value=format_items(data.get("egg")),
                    inline=False
                )
                embed.add_field(
                    name="🍯 Event Shop",
                    value=format_items(data.get("honey")),
                    inline=False
                )
                embed.add_field(
                    name="🧳 Traveling Merchant",
                    value=format_items(data.get("travelingmerchant")),
                    inline=False
                )

                if posted_message:
                    await posted_message.edit(embed=embed)
                else:
                    posted_message = await channel.send(embed=embed)

        except Exception as e:
            print(f"Failed to fetch stock data: {e}")

bot.run(TOKEN)
