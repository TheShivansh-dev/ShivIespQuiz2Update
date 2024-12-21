from flask import Flask
import os
import asyncio
import sys


app = Flask(__name__)

async def shutdown():
    print("Shutting down gracefully...")
    await asyncio.sleep(2)  # Simulate cleanup process
    sys.exit(0)

def handle_sigterm(signum, frame):
    asyncio.run(shutdown())





@app.route('/')
def helloworld():
    return "grey word"


async def run_bot():
    # Replace this with your bot logic
    while True:
        print("Bot is running...")
        await asyncio.sleep(5)

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Run Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Run bot asyncio loop
    try:
        asyncio.run(run_bot())
    except:
        print("Shutting down...")
