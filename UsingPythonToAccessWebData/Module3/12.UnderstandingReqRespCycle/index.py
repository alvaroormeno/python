import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysocket.close()





# The snippet above is an example of a client program that uses sockets to make a connection to a web server.
# The program makes a connection to port 80 on the server www.py4e.com.
# The program sends a GET request for the file romeo.txt.
# The program then loops, reading data in 512-character chunks until there is no more data to read.
# The program then closes the socket and exits.
# The program uses encode() to convert the string into bytes before sending it over the socket.
# The program uses decode() to convert the bytes into a string after reading it from the socket.
# The program uses end='' to prevent Python from printing a newline after each print statement.
