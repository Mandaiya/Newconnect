from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import RPCError
import sys

# Replace with your actual API credentials
api_id = 24440655
api_hash = 'eeaa77abb90cbc1a90b9890999c44421'

try:
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        session_string = client.session.save()

        print("\n✅ Here is your session string:\n")
        print(session_string)
        print("\n⚠️ Copy and store it safely! Do NOT share it with anyone!\n")

        async def send_string_to_user():
            try:
                me = await client.get_me()
                text = f"""
Hello {me.first_name}, this is your **Telethon String Session**.  
⚠️ **Do NOT share it with anyone**—they can take full control of your account!

{session_string}


✅ **It has been saved to your Saved Messages for security.**
"""
                await client.send_message("me", text)
                print("\n✅ Session string successfully sent to your Saved Messages.")

            except RPCError as e:
                print(f"\n❌ Telegram RPCError: {e}")
                sys.exit(1)
            except Exception as e:
                print(f"\n❌ Unexpected Error: {e}")
                sys.exit(1)

        client.loop.run_until_complete(send_string_to_user())

except ValueError as e:
    print(f"\n❌ Invalid API credentials: {e}")
    sys.exit(1)
except RPCError as e:
    print(f"\n❌ Telegram RPCError: {e}")
    sys.exit(1)
except ConnectionError:
    print("\n❌ Failed to connect to Telegram servers. Check your internet connection.")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")
    sys.exit(1)