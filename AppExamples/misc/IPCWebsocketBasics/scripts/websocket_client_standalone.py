# websocket_client_standalone.py
#
# ZEISS INSPECT Inter Process Communication (IPC) via Websocket Example
#
# Socket Client - Transmits a command encoded as JSON string and receives a response 
#
# Standalone Python script - run from Windows command line
#
# Carl Zeiss GOM Metrology GmbH, 2025
#
# This App is part of the ZEISS INSPECT Python API Examples:
# https://zeiss.github.io/zeiss-inspect-app-api/2025/python_examples/examples_overview.html
# ---

import asyncio
import websockets
from websockets.asyncio.client import connect

HOST = 'localhost'
"""string: Hostname or IP address"""

PORT = 40010
"""int: TCP/IP port"""

URI = f"ws://{HOST}:{PORT}"
"""string: Websocket URI"""

async def transmit_receive(payload):
    """Transmit payload via Websocket and receive response"""
    try:
        async with connect(URI) as websocket:
            print(f"{payload} ->")
            try:
                await websocket.send(payload)
                response = await websocket.recv()
            except websockets.exceptions.ConnectionClosed as e:
                print(f"Connection closed: {e.code}, reason: {e.reason}")
            except Exception as e:
                print(f"An error occurred: {e}")
            else:
                print(f"<- {response}")
    except Exception as e:
        print(f"An error occurred: {e}")


REQUEST = '{"element": "circle", "center": ["1.0", "-2.0", "3.0"], "radius": "10.0"}'
asyncio.run(transmit_receive(REQUEST))

# This will quit the server (optional)
#asyncio.run(transmit_receive("quit"))
