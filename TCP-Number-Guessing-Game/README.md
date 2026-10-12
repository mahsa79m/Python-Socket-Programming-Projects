# TCP Number Guessing Game

A Python socket-based number guessing game using a TCP client and a multithreaded server.

## Features

- Server selects a random number between 1 and 100 for each client connection.
- Client sends guesses and receives `Higher`, `Lower`, or `Correct`.
- Client checks that the input consists of digits.
- Server handles multiple client connections using Python threads.
- Basic connection and socket error handling.

## Run

Open two terminals in this folder. Start the server first:

```bash
python GameServer.py
```

Then start the client:

```bash
python Client.py
```

Enter guesses until the server responds `Correct`. The server listens on `127.0.0.1:11111`.

## Files

- `GameServer.py` — TCP server and per-client game logic.
- `Client.py` — command-line TCP client.

## Limitations

The application uses a simple message exchange without explicit message framing. The input check does not enforce the 1–100 range. The client has a 10-second socket timeout, which can interrupt a session if the server does not reply in time. This is a command-line application; no web interface is included.

The enhanced source is preserved as provided and has not been independently end-to-end tested for this release.
