import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class PaymentView(discord.ui.View):
    @discord.ui.button(label="💵 Open Cash App", style=discord.ButtonStyle.green)
    async def cashapp(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "https://cash.app/$jamarialittle0",
            ephemeral=True
        )

    @discord.ui.button(label="🅿️ Open PayPal", style=discord.ButtonStyle.blurple)
    async def paypal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "https://paypal.me/stagesteal",
            ephemeral=True
        )

    @discord.ui.button(label="🏦 View Chime", style=discord.ButtonStyle.gray)
    async def chime(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "$Questishim",
            ephemeral=True
        )

    @discord.ui.button(label="✅ I've Paid", style=discord.ButtonStyle.red)
    async def paid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Please upload proof in the ticket.",
            ephemeral=True
        )

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="payments", description="Show payment methods")
async def payments(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🔴 Eyevision • Payment Methods",
        color=discord.Color.red()
    )

    embed.add_field(name="💵 Cash App", value="$jamarialittle0", inline=False)
    embed.add_field(name="🅿️ PayPal", value="paypal.me/stagesteal", inline=False)
    embed.add_field(name="🏦 Chime", value="$Questishim", inline=False)

    embed.set_footer(text="Click I've Paid after sending payment proof.")

    await interaction.response.send_message(embed=embed, view=PaymentView())

bot.run(os.getenv("DISCORD_TOKEN"))
