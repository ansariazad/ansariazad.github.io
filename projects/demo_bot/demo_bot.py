"""
Demo Telegram Bot — Portfolio Showcase
A working bot template Azad can deploy and show to clients.
Run: pip install python-telegram-bot && python demo_bot.py
"""
import os
import datetime
import json
import random

# ── If python-telegram-bot is installed, run as real bot
# ── Otherwise, this serves as a clean code sample for portfolio

DEMO_RESPONSES = {
    "weather": "☀️ Mumbai: 32°C, Humidity 75%, Partly Cloudy",
    "quote": [
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Code is like humor. When you have to explain it, it's bad.",
        "First, solve the problem. Then, write the code.",
        "Simplicity is the soul of efficiency.",
    ],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "A SQL query walks into a bar, walks up to two tables and asks: Can I join you?",
        "How many programmers does it take to change a light bulb? None. That's a hardware problem.",
    ],
}


class SmartBot:
    """A demo bot showcasing clean Python architecture."""

    def __init__(self, name: str = "AzadBot"):
        self.name = name
        self.start_time = datetime.datetime.now()
        self.commands_handled = 0
        self.users = {}

    def handle_start(self, user_id: int, username: str) -> str:
        self.users[user_id] = {"name": username, "joined": str(datetime.datetime.now())}
        self.commands_handled += 1
        return (
            f"Hey {username}! I'm {self.name}.\n\n"
            "Here's what I can do:\n"
            "/weather — Current weather\n"
            "/quote — Random inspiration\n"
            "/joke — Developer humor\n"
            "/stats — Bot statistics\n"
            "/help — Show this menu"
        )

    def handle_weather(self) -> str:
        self.commands_handled += 1
        return DEMO_RESPONSES["weather"]

    def handle_quote(self) -> str:
        self.commands_handled += 1
        return random.choice(DEMO_RESPONSES["quote"])

    def handle_joke(self) -> str:
        self.commands_handled += 1
        return random.choice(DEMO_RESPONSES["joke"])

    def handle_stats(self) -> str:
        self.commands_handled += 1
        uptime = datetime.datetime.now() - self.start_time
        return (
            f"📊 {self.name} Stats\n"
            f"├─ Uptime: {uptime}\n"
            f"├─ Commands handled: {self.commands_handled}\n"
            f"├─ Users: {len(self.users)}\n"
            f"└─ Status: Running ✓"
        )

    def handle_message(self, text: str, user_id: int = 0, username: str = "User") -> str:
        text = text.strip().lower()
        routes = {
            "/start": lambda: self.handle_start(user_id, username),
            "/help": lambda: self.handle_start(user_id, username),
            "/weather": self.handle_weather,
            "/quote": self.handle_quote,
            "/joke": self.handle_joke,
            "/stats": self.handle_stats,
        }
        handler = routes.get(text)
        if handler:
            return handler()
        return f"I don't understand '{text}'. Type /help to see what I can do."


# ── Telegram Integration (if token is set) ──
def run_telegram_bot():
    """Run as a real Telegram bot if BOT_TOKEN is set."""
    try:
        from telegram import Update
        from telegram.ext import Application, CommandHandler, MessageHandler, filters

        token = os.environ.get("BOT_TOKEN")
        if not token:
            print("No BOT_TOKEN found. Running in demo mode.\n")
            return run_demo()

        bot = SmartBot()

        async def start(update: Update, context):
            user = update.effective_user
            reply = bot.handle_start(user.id, user.first_name)
            await update.message.reply_text(reply)

        async def weather(update: Update, context):
            await update.message.reply_text(bot.handle_weather())

        async def quote(update: Update, context):
            await update.message.reply_text(bot.handle_quote())

        async def joke(update: Update, context):
            await update.message.reply_text(bot.handle_joke())

        async def stats(update: Update, context):
            await update.message.reply_text(bot.handle_stats())

        async def echo(update: Update, context):
            reply = bot.handle_message(update.message.text, update.effective_user.id, update.effective_user.first_name)
            await update.message.reply_text(reply)

        app = Application.builder().token(token).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", start))
        app.add_handler(CommandHandler("weather", weather))
        app.add_handler(CommandHandler("quote", quote))
        app.add_handler(CommandHandler("joke", joke))
        app.add_handler(CommandHandler("stats", stats))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

        print(f"🤖 {bot.name} is running on Telegram...")
        app.run_polling()

    except ImportError:
        print("python-telegram-bot not installed. Running demo mode.\n")
        run_demo()


def run_demo():
    """Interactive demo mode — shows the bot working in terminal."""
    bot = SmartBot()
    print(f"═══ {bot.name} Demo Mode ═══")
    print("Type commands like /start, /weather, /quote, /joke, /stats")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ("quit", "exit", "q"):
                print("Bye!")
                break
            response = bot.handle_message(user_input, user_id=1, username="Demo User")
            print(f"Bot: {response}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break


if __name__ == "__main__":
    run_telegram_bot()
