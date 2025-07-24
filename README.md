# simple-c2-demonstration
This is a basic C2 (Command &amp; Control) Server - Client configuration, using python socket.

## Start the server
`python3 server.py`
If using default values, it will only listen on 127.0.0.1 (localhost) on port 7053.

## Start the client
`python3 client.py`
If using default values, it will send data to 127.0.0.1:7053

## TODOs

- [ ] Encrypt data transmitted

It could be an interesting thing to combine it with https://github.com/gderybel/simple-ransomware-demonstration/, so you could send the encryption key to the server.
