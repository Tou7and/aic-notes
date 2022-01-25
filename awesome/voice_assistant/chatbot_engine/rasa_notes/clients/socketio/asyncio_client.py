import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')


@sio.event
async def disconnect():
    print('disconnected from server')


async def main():
    await sio.connect('http://localhost:5005')
    await sio.emit('user_uttered', {"session_id": "rx782", "message": "Hi!"})
    print(sio.on("bot_uttered"))
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
