import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import time
from deep_translator import GoogleTranslator
import signal
import sys

def translate_text(text, target="en"):
    return GoogleTranslator(source='auto', target=target).translate(text)



api_id = 35159329
api_hash = '3b4f3d55299cbbb398c8f7254782d7b3'
session_string = "1BJWap1wBu5WedHJZzGOgekV0K16emgiJMf_BRwFGWtgb2-7Z7yL_djzQPMsS2M-KEjr2k1PtEHFgvU9xtr7qg8wiQNbbojYiOAZobptQnDhgnFou_4pH8bc437IcOvApvLPxN2EINzZMTWSDVyTdTDA3jkczMBrCA8ocDIljEYuc07fk2KOdk_gvyLOWCpB3qK7ziUgD0-OSs3semPKIFkGp7K6QNujpkaOrm0iC4XX4o5p02-4gVwusTvS9Ny9B0crUb4pcpnZZ0mIStD6pVaueRyq9pIb5GukqtD2TV9mWUjDrM6dU6ythYgYZgIFY48Tx6Bghio7Y5FUGXXRWG3AVEFK3flU="

TARGET_CHANNELS = [
    -1001310984791,
    -1002036270701,
    -1001134494888,
    -1001458480018,
]
# source_channel = os.getenv("SOURCE_CHANNEL")
# target_channel = os.getenv("TARGET_CHANNEL")
time.sleep(30)
client = TelegramClient(StringSession(session_string), api_id, api_hash)


def shutdown_handler(signum, frame):
    print("Shutting down...")
    try:
        client.disconnect()
    except:
        pass
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

@client.on(events.NewMessage(chats=TARGET_CHANNELS))
async def handler(event):
    channel = await client.get_entity(-1003731587014)
    await client.forward_messages(channel, event.message)
    tran_msg = GoogleTranslator(source='english', target='arabic').translate(event.message.text)
    await client.send_messages(channel, trans_msg)
     

async def main():
    await client.start()
    channel = await client.get_entity(-1003731587014)
    await client.send_message(channel, "Bot is running...")
    print("Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
