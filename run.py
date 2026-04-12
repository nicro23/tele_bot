from telethon import TelegramClient, events
import logging
import asyncio
logging.basicConfig(format='[%(levelname) %(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
# Use your own values from my.telegram.org
api_id = 35159329
api_hash = '3b4f3d55299cbbb398c8f7254782d7b3'

# The first parameter is the .session file name (absolute paths allowed)
client = TelegramClient('anon2', api_id, api_hash)
await client.start()
TARGET_CHANNELS = [
    -1001310984791,
    -1002036270701,
    -1001134494888,
    -1001458480018,
]
@client.on(events.NewMessage(chats=TARGET_CHANNELS))
async def my_event_handler(event):
      # await client.send_message(channel, event.raw_text)
      await client.forward_messages(target_channel, event.message)

async def fun():
  channel = await client.get_entity(-1003731587014)
  # async for dialog in client.iter_dialogs():
  #   print(dialog.name, 'has ID', dialog.id)
  # async for dialog in client.iter_dialogs():
  #   if dialog.is_channel:
  #       print(dialog.name, dialog.id)
  # async for message in client.iter_messages('me'):
  #       print(message.id, message.text)
  while True:
        # print("running...")
        await asyncio.sleep(5)
  # await client.send_message(channel, 'shutting down')
  await client.disconnect()

await fun()
