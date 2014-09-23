# HTTP Response

## Response line
### Status line
The **status line** is the first line of the response provided by the server. It
consists of three parts:
- The HTTP version.
- A response code that provides the result of the content.
- An English reason phrase describing the status code.

Examples: `HTTP/1.1 200 OK` or  `HTTP/1.1 404 Not Found`

### Status code
The **status code** associated with the status line belong to done of five
categories:

- Provisional Response
- Successful
- Redirected
- Request Error
- Server Error

## Headers
Allow the server to pass additional information about the response. These header
fields have the same format as in the request.  Ex `Accept-Ranges`, `Age`, `Location`, `Proxy-Authenticate`.

## Message body
The requested resource, for example, the actual HTML, is included in the
message body of the response.

## HTTP Secure
The HTTP Secure protocol (HTTPS) is a combination of HTTP and SSL/TLS protocols.
HTTPS enhances the HTTP protocol by providing encrypted communication and
secure web server identification.
