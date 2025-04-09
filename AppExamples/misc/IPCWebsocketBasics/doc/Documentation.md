# IPCWebsocketBasics

This is a minimal example for triggering command execution in ZEISS INSPECT via the WebSocket protocol. In a broader sense, this example demonstrates how Inter Process Communication (IPC) via the WebSocket protocol can be used to connect ZEISS INSPECT to other applications.

Extend this App with custom commands and responses as needed.

## WebSocket Server

The ZEISS INSPECT App `websocket_server_app.py` waits for connections on the WebSocket interface defined by `ws://<HOST>:<PORT>` and expects requests as strings. The server receives a request, sends a response and continues waiting for a new connection.
The server terminates if the server sends 'quit' as request.

### Requests

1. JSON String

   Any valid JSON string can be used for encoding commands and parameters. The server may send a string as response.

2. **Syntax:** 'quit'
   
   The command 'quit' terminates the server. The server sends 'bye' as response.

## WebSocket Client

The client `websocket_client_standalone.py` is implemented as a standalone Python program. Install the `websockets` package in your Python environment, wxport the client script from the App, and run it from the Windows command line with `python websocket_client_standalone.py`.

The client's requests and the server's responses are printed to the Windows console.

## Testing or debugging the server

You can test the server by running the following from the command line:

```
python -m websockets ws://<host>:<port>/
```

**Example:**
```
python -m websockets ws://localhost:40010/
Connected to ws://localhost:40010/.
> {"elements": {"file": "C:/temp/Points.gxml", "import_mode": "clipboard"}}
< Ok
> {
< Error: Malformed JSON message.
> quit
< bye
>
Connection closed.
```

# References

* [RFC 6455: The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
* [Python websockets library documentation](https://websockets.readthedocs.io/en/stable/index.html)
* [IPCWebsocketExample](https://github.com/ZEISS/zeiss-inspect-app-examples/tree/main/AppExamples/misc/IPCWebsocketExample)
