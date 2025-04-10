#
# websocket_server_app.py
#
# ZEISS INSPECT Inter Process Communication (IPC) via Websocket
#
# Websocket Server App
# 
# The server is listening on host <HOST> port <PORT> for requests.
# 
# The following requests are implemented:
# 1. Any JSON string
#    The JSON string is parsed into 'command' and passed to 'handle_command()'
#
# 3. quit
#    Close the connection and terminate the App.
#
# For each request, a response is sent as plain text.
#
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import json
import asyncio

import websockets
from websockets.asyncio.server import serve

HOST = 'localhost'
PORT = 40010

def handle_command(command):
    """
    Command handler
    
    Params:
        command (dict): Your custom command
        
    Returns:
        string: Response
    """
    print(f"handle_command(): {command}")
    return "Ok"

async def server(websocket):
    """Websocket server"""

    async for request in websocket:
        # Websocket request handler
        print(f"{request=}")

        if request.startswith("quit"):
            await websocket.send("bye")
            await websocket.close(code=1000, reason="Closing connection.")
            print("Connection closed by client.")
            asyncio.get_event_loop().stop()
            return

        try:
            command = json.loads(request)
        except json.JSONDecodeError:
            response = "Error: Malformed JSON message."
        else:
            # Decode JSON message
            response = handle_command(command)

        try:
            await websocket.send(response)
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed by the client.")
            asyncio.get_event_loop().stop()
            return

    await websocket.close(code=1000, reason="Closing connection.")

async def main():
    """Main function"""
    print(f"Websocket server waiting for requests at ws://{HOST}:{PORT}")
    async with serve(server, HOST, PORT):
        await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        pass
