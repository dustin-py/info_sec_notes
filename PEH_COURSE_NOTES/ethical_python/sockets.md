# **Sockets**
---
***A way to connect 2 ports together***
- we will use sockets to connect to an open port and ip address

- **socket**: python module

- ***EX Simple Socket Script***:

        #!/bash/python3
        import socket 

        HOST = '127.0.0.1' <-- host to scan
        PORT = 7777 <-- port to connect

        s = socket.socket(
            socket.AF_INET,  <-- specify IPv4
            socket.SOCK_STREAM) <-- its a port
        
        s.connect(
            (HOST, PORT))

`NC -NVLP <PORT TO LISTEN>`

- This just connects to a socket