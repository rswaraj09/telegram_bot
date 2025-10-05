from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = ""  # Replace with your actual bot token


async def start(update: Update, context):
    """Send a message with donation options when the user starts the bot."""
    keyboard = [
        [InlineKeyboardButton("📦 Donate Rice", callback_data="donate_rice")],
        [InlineKeyboardButton("🧂 Donate Salt", callback_data="donate_salt")],
        [InlineKeyboardButton("🌾 Donate Wheat", callback_data="donate_wheat")],
        [InlineKeyboardButton("📝 Donate Stationary Items", callback_data="donate_stationary_items")],
        [InlineKeyboardButton("💰 Donate Money", callback_data="donate_money")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🛠️ **Welcome to SankalpSeva!** 🌍\n"
        "We connect donors with orphanages, elderly homes, and food providers to ensure your donations make a real impact. "
        "Your generosity can bring meaningful change!\n\n"
        "**Together, let's make a difference! 💙**\n\n"
        "What would you like to donate?",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def button_click(update: Update, context):
    """Handle button clicks."""
    query = update.callback_query
    await query.answer()

    responses = {
        "donate_rice": "🍚 You chose to **Donate Rice**. You can Donate through this button👇👇\n\n[Donate Here](https://www.paypal.com/ncp/payment/KVMV7XHJG93EC)",
        "donate_salt": "🧂 You chose to **Donate Salt**. You can Donate through this button👇👇\n\n[Donate Here](https://www.paypal.com/ncp/payment/V5FTZVSE9V3S8)",
        "donate_wheat": "🌾 You chose to **Donate Wheat**. You can Donate through this button👇👇\n\n[Donate Here](https://www.paypal.com/ncp/payment/B8ATMU59T3EUG)",
        "donate_stationary_items": "📝 You chose to **Donate Stationary Items**. You can Donate through this button👇👇\n\n[Donate Here](https://www.paypal.com/ncp/payment/4ED2NW75432MW)",
        "donate_money": "💰 You chose to **Donate Money**. You can Donate through this button👇👇\n\n[Donate Here](https://www.paypal.com/ncp/payment/JYLW89UF3GCKU)"
    }

    if query.data in responses:
        await query.edit_message_text(text=responses[query.data] + "\n\n**🙏 Thank you for your kindness and generosity! Your contribution will make a meaningful difference in the lives of those in need. Every act of giving brings hope and positivity, and we deeply appreciate your support in creating a better world. Together, we can spread kindness and uplift communities! 💙✨**", parse_mode="Markdown")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))

print("🤖 Bot is running...")
app.run_polling()
