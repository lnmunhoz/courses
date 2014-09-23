# Rails Controllers - Request Handling

## Action Pack
View and controllers on Rails are supported by **Action Pack**, which consists
of three Ruby modules: `ActionDispatch`, `ActionController` and `ActionView`.

### Dispatcher
When an HTTP request is made, the `ActionDispatch` module is used to map the
request to a particular controller action. Requests are mapped to controller
actions via `routes`.

To connect a request to a controller action, you add a route to `./config/routes.rb`.
Ex. Adding the following `get 'products/:id' => 'catalog#view'` will map the
request to the **catalog controller** with a **method** called **view**
