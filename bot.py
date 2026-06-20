import discord
import os
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


class PaymentView(discord.ui.View):
def init(self):
super().init(timeout=None)

@discord.ui.button(label="💵 Open Cash App", style=discord.ButtonStyle.green)
async def cashapp(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(
        "Cash App: https://cash.app/$jamarialittle0\nNOTE: FOOD",
        ephemeral=True
    )

@discord.ui.button(label="🅿️ Open PayPal", style=discord.ButtonStyle.blurple)
async def paypal(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(
        "PayPal: https://paypal.me/stagesteal\nNOTE: FRIENDS AND FAMILY",
        ephemeral=True
    )

@discord.ui.button(label="🏦 View Chime", style=discord.ButtonStyle.gray)
async def chime(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(
        "Chime: $Questishim",
        ephemeral=True
    )

@discord.ui.button(label="✅ I've Paid", style=discord.ButtonStyle.red)
async def paid(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(
        "Please upload a screenshot of your payment proof in this ticket so staff can verify it.",
        ephemeral=True
    )

@bot.tree.command(name="payments", description="Show Eyevision payment methods")
async def payments(interaction: discord.Interaction):

embed = discord.Embed(
    title="🔴 Eyevision • Payment Methods",
    description="Choose a payment method below and follow the notes provided.",
    color=discord.Color.red()
)

embed.add_field(
    name="💵 Cash App",
    value="$jamarialittle0\n**NOTE:** FOOD",
    inline=False
)

embed.add_field(
    name="🅿️ PayPal",
    value="https://paypal.me/stagesteal\n**NOTE:** FRIENDS AND FAMILY",
    inline=False
)

embed.add_field(
    name="🏦 Chime",
    value="$Questishim",
    inline=False
)

embed.set_footer(
    text="After paying, click 'I've Paid' and upload your proof in this ticket."
)

await interaction.response.send_message(
    embed=embed,
    view=PaymentView()
)

@bot.event
async def on_ready():
try:
synced = await bot.tree.sync()
print(f"Logged in as {bot.user}")
print(f"Synced {len(synced)} command(s)")
except Exception as e:
print(f"Sync error: {e}")


bot.run(os.getenv("DISCORD_TOKEN"))
