import sys
import socketio

user_id = "thefool"
user_message = "hi"

def botUtterTask(user_id, user_message):
    sio = socketio.Client()

    @sio.on('connect')
    def on_connect():
        print('Connected to the Rasa Socket Server')
    sio.connect('http://localhost:5500')

    # sio.emit('session_request', {'session_id': user_id})
    # sio.emit('user_uttered', {'message': user_message})
    sio.emit("user_uttered", {"session_id": user_id, "message": user_message})

    @sio.on('bot_uttered')
    def on_message(data):
        print(data)

print(botUtterTask(user_id, user_message))
