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
session_string = "1BJWap1wBuy7Iob2bc0i0H_uqjM8w6pXz3t7oSJYHkNVWOj39A33K0C9FS3og39rXhFSSn8EYlHENzz6iKmSk74xHvrWxLxW7xVcjbWOhaTpKROkU6XcVCQS1O5GB1hszxs3VpTud1V9k_cSGdQQWC1xx5qqoOaO5W1y-AfaXYRi5nXh-vd2_aCEkIwYQ9tdvGoXKxyVxJR8BnDsyy8KyOdIawA3Vpc0d20yCFrAYgLkmQn8ux_fNChMVmHB060Iec5oXYRxfQMHYP5Qnln05NCyhAR6ust4kYReIrpH9d12-l_hzsfNBmMNwoZ__ZcBWLVhH1lPgylkjBaQKwvPBKskNZZ_Lsg4="
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

async def main():
    await client.start()
    channel = await client.get_entity(-1003731587014)
    await client.send_message(channel, "Bot is running...")
    print("Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
