# Telegram Bot

Simple Telegram bot project.

This repository contains a small Telegram bot implemented in Python. It uses a modular `handlers/` folder for message handling and a `config.py` for configuration.

## Requirements

- Python 3.8 or newer
- A Telegram bot token (from @BotFather)

## Quick start (Windows PowerShell)

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Note: If PowerShell blocks script execution, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in an elevated PowerShell, or activate the venv using Command Prompt with `.\.venv\Scripts\activate.bat`.

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Configure the bot token.

- Option A — Edit `config.py`, `bot.py` and set your `BOT_TOKEN` variable.
- 

```
BOT_TOKEN=123456:ABC-DEF...your_token_here
```

Make sure your `config.py` reads from the environment when appropriate.

4. Run the bot:

```powershell
python bot.py
```

## Project structure

- `bot.py` — Bot entry point (starts the updater/loop).
- `config.py` — Configuration (token, settings). Replace or set the `BOT_TOKEN` value.
- `requirements.txt` — Python dependencies.
- `handlers/` — Message and command handlers:
  - `start_handler.py` — Handler for the /start command.
  - `message_handler.py` — Generic message handling logic.

## Development notes

- Keep secrets (bot token) out of version control. Add `.env` and/or your virtual environment folder to `.gitignore`.
- If you add webhooks or deploy to a server, update `bot.py` accordingly.

## Usage

How to use the bot once it's running locally or deployed.

- `/start` — Starts a conversation with the bot. Typically `start_handler.py` sends a short welcome message and brief instructions.
- `/help` — (If implemented) shows available commands or help text.
- Sending any plain message — `message_handler.py` handles non-command messages. In many simple setups this will echo or reply with a short acknowledgement.

Notes on assumptions: this README assumes `start_handler.py` sends a friendly greeting and `message_handler.py` replies to or echoes messages. If your handler implementations differ, update them or this README accordingly.

### Examples (what to send and expected responses)

1. Send the `/start` command in a chat with the bot.

  Expected (example) reply:

  "Hello! I'm your bot. Send /help to see available commands."

2. Send a plain message like "Hello bot".

  Expected (example) reply if the message handler echoes:

  "You said: Hello bot"

3. Send `/help` (if implemented).

  Expected (example) reply:

  "Available commands:\n/start - Start the bot\n/help - Show this message"

These examples are intentionally generic — update the text to match the exact responses implemented in your handlers.

## Troubleshooting

- "Bot does not respond": verify `BOT_TOKEN`, ensure network access, and check any error logs printed by `bot.py`.
- "Permission denied" when activating venv on PowerShell: see the execution policy note above.

## Contributing

Contributions are welcome. Open issues or submit pull requests with clear descriptions and tests where appropriate.

## License

This project is provided as-is. Add a license file if you want to license it formally.


