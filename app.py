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

if __name__ == "__main__":
   port = int(os.environ.get('PORT', 8080))
   app.run(host='0.0.0.0', port=port)
   try:
        asyncio.get_event_loop().run_forever()
   except :
        print("App interrupted!")
