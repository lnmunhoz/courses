# The Hypertext Transfer Protocol (HTTP) Introduction
HTTP is an application layer protocol used to delivery resources in distributed
hypermedia information systems. The HTTP protocol is extremely lightweight and
and simple.

## Background

### HTTP/0.9
The first documented HTTP protocol was *HTTP/0.9*, a client could only issue
*GET* requests. Ex. `GET /welcome.html`

### HTTP/1.0
The *HTTP/1.0* protocol, introduced in 1996, extended the *HTTP/0.9* to include
request headers along with additional request methods.

### HTTP/1.1
- Faster response, allowing multiple transactions to take place over a single
persistent connection.
- Bandwidth saving, by adding cache support.
- Dinamically generated content, by supporting chunked encoding, wich allows
a response to be sent before its total length is known.
- Efficient use of IP addresses, multiple domains can be served from a single
IP address.
- Support for proxies.

## Sessions
An HTTP session proceeds as follows:
1. An HTTP client estabilishes a TCP connection to a particular port on a
host server and initiates a request. Estabilishing the TCP connection may
first involve using an DNS server in order to obtain the IP adress.
2. An HTTP server listening on that port waits for a client's request message.
3. Upon receiving the request, the server processes it and send back a status
line, such as "HTTP 1/1 200 OK", along with a message of its own.
