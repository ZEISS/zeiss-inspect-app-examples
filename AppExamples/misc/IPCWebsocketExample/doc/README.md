# IPCWebsocketExample

This is an example for triggering command execution in ZEISS INSPECT via the WebSocket protocol. In a broader sense, this example demonstrates how Inter Process Communication (IPC) via the WebSocket protocol can be used to connect ZEISS INSPECT to other applications.

## WebSocket Server

The ZEISS INSPECT App TestServerApp.py waits for connections on the WebSocket interface defined by `ws://<HOST>:<PORT>` and expects requests as strings. The server receives a request, sends a response and starts waiting for a new connection.
Press **Esc** in the ZEISS INSPECT main window or close the client window to stop the server.

### Requests

Three types of requests are supported:

1. **Import image from file**

   If it does not exist yet, the requested measurement series is created with the command gom.script.sys.create_measurement_series_for_other_images().

    Then, the image is imported with the command gom.script.sys.import_other_images ()

2. **Import elements from file**
   
    The elements are imported with the command gom.script.sys.import_gom_inspection_exchange(). 

3. **Quit**
   
   Close the interface and terminate the server.

### Responses

The server responds with "O.k." if the request was decoded successfully, otherwise it sends an error message as plain text.

## WebSocket Client

The client TestClientStandalone.py is implemented as a standalone Python program with a PySide 6 GUI. Export the client script from the App and started it from the Windows command line with `python TestClientStandalone.py`.
After selecting the request parameters, click **Transmit image request** or **Transmit elements request**. The server's response is printed in the text widget labelled 'Status'.
 