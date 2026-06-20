import discord
import os
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


# ---------- PAYMENT BUTTONS ----------
class PaymentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="💵 Cash App", style=discord.ButtonStyle.green)
    async def cashapp(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "https://cash.app/$jamarialittle0",
            ephemeral=True
        )

    @discord.ui.button(label="🅿️ PayPal", style=discord.ButtonStyle.blurple)
    async def paypal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "https://paypal.me/stagesteal",
            ephemeral=True
        )

    @discord.ui.button(label="🏦 Chime", style=discord.ButtonStyle.gray)
    async def chime(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "$Questishim",
            ephemeral=True
        )

    @discord.ui.button(label="✅ I've Paid", style=discord.ButtonStyle.red)
    async def paid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Please upload your payment proof in the ticket so staff can verify it.",
            ephemeral=True
        )


# ---------- SLASH COMMAND ----------
@bot.tree.command(name="payments", description="Show Eyevision payment methods")
async def payments(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🔴 Eyevision • Payment Methods",
        color=discord.Color.red()
    )

    embed.add_field(name="💵 Cash App", value="$jamarialittle0", inline=False)
    embed.add_field(name="🅿️ PayPal", value="https://paypal.me/stagesteal", inline=False)
    embed.add_field(name="🏦 Chime", value="$Questishim", inline=False)

    await interaction.response.send_message(
        embed=embed,
        view=PaymentView()
    )


# ---------- SYNC + READY ----------
@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"Logged in as {bot.user} and commands synced")
    except Exception as e:
        print(f"Sync error: {e}")


# ---------- RUN BOT ----------
bot.run(os.getenv("DISCORD_TOKEN"))
