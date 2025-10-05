def reply(update, context):
    user_message = update.message.text
    update.message.reply_text(f"You said: {user_message}")
