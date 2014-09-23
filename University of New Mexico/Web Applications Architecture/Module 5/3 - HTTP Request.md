# HTTP Request
An HTTP/1.1 request message consists of three parts:
- Request line
- Header
- Message body

## Request line
The Request line identifies the resource, along with the desired action that
should be applied to it. The resource is typically identified by a URI (Universal
Resource Identifier).

There are nine request types that can be specified:
- **HEAD** - Its a GET request, without a response body.

- **GET** - Returns a representation of the resource.

- **POST** - Submit data to the resource, where the data is supplied in the body of the
request.

- **PUT** - Submit a representation of the resource.

- **DELETE** - Delete the resource.

- **TRACE** - Echoes back the received requested.

- **OPTIONS** - Returns the HTTP methods that the server supports for the
specified resource.

- **CONNECT** - Converts the request connection to a transparent TCP/IP tunnel.

- **PATCH** - Apply partial modifications to a resource.

HEAD, GET, OPTIONS and TRACE are referred to as **safe methods**. This methods
should not produce side effects to the server.

In contrast, POST, PUT and DELETE methods may cause side effects on the server.
Furthermore, the PUT and DELETE methods should be **idempontent**, wich means
that multiple identical requests should have the same effect as a single request.

## Header
The HTTP message header is the primary part of a HTTP request. It contains
the operating parameters. Header fields starts with the field name, followed by
a colon, and then the field value. Ex `Accept: plain/text`.

## Message body
The message body typically includes user-entered data or files that are being
upload to the server. Ex `Content-Type: text/html` or `Content-Type: image/gif`.
