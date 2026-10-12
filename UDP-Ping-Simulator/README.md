# UDP Ping Simulator

A simple Python UDP client-server example that measures round-trip response time and simulates packet loss.

## Features

- Sends four UDP requests from the client.
- Measures round-trip time using `time.perf_counter()`.
- Displays `Request timeout` if a reply is not received within one second.
- Server randomly responds to or drops incoming requests.

## Run

Open two terminals in this folder. Start the server first:

```bash
python server.py
```

Then start the client:

```bash
python client.py
```

The server listens on `127.0.0.1:22222`. Stop the server with Ctrl+C.

## Files

- `server.py` — UDP server with randomized responses.
- `client.py` — UDP client that sends four requests and reports timings.

## Limitations

This is an application-level UDP ping simulation, not ICMP ping. Requests are not tagged with unique sequence identifiers, and packet loss is simulated randomly. The source is the author's original working version; it has not been independently re-tested in this packaging step.
