import asyncio
from telethon import TelegramClient, events
import os

api_id = 35159329
api_hash = '3b4f3d55299cbbb398c8f7254782d7b3'
TARGET_CHANNELS = [
    -1001310984791,
    -1002036270701,
    -1001134494888,
    -1001458480018,
]
# source_channel = os.getenv("SOURCE_CHANNEL")
# target_channel = os.getenv("TARGET_CHANNEL")

client = TelegramClient('anon2', api_id, api_hash)

@client.on(events.NewMessage(chats=TARGET_CHANNELS))
async def handler(event):
    await client.forward_messages(channel, event.message)

async def main():
    await client.start()
    channel = await client.get_entity(-1003731587014)
    print("Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
