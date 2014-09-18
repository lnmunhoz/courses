# What is Middleware?

You can make an analogy that **middleware** is the software that provides to
applications beyond those available from the underlying operating system. It
connects applications running on the server side, and passes data between them.

## Rails Middleware
In Rails, a middleware stack called **Rack** is automatically provided. It is
responsible for  handling HTTP requests and responses.

### Rack
Rack is used to organize modules. `Rack::Builder` puts these together, creating
a stack-like structure.

To see the middleware installed in a Rails application, from the root of the
project, type:
```ruby
$ rake middleware
```
When you execute `$ rails server`, a `Rack::Server` object is created (WEBrick
by default), and the middleware components are loaded up. The `Rack::Server#start`
method starts the web server listening on the designated port for HTTP requests.
