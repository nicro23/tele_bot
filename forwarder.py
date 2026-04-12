import asyncio
from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

source_channel = os.getenv("SOURCE_CHANNEL")
target_channel = os.getenv("TARGET_CHANNEL")

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await client.forward_messages(target_channel, event.message)

async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
