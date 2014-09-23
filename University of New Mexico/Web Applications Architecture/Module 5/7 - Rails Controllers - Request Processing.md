# Rails Controller - Request Processing

The HTTP Get request: `http:localhost:3000/posts/1` will route to the `show`
method in the `PostsController` class, passin `params[:id]` with a value of 1
to the controller. Next, the `show` method will use the `ActiveRecord#find`
method to retrieve the post with id = 1 from the database, and assign it to the
instance variable `@post`. Finally, the controller will pass `@post` to the view
to the template file: `.app/views/posts/show.html.erb` and this will be used
to create the HTML that will be sent to the browser.

## Filters
The `PostController@show` method is defined as follows:
```ruby
# GET /posts/1
# GET /posts/1.json
def show
end
```
The desired post is actually retrieved from the database using a `filter` called
`set_post`. Filters allow controllers to run shared pre and post-processing code
over their methods.

## Sessions
Session data is stored in Rails using a hash structure that persists across
requests, and can be accessed by controllers. Ex. `session[:current_user] = user.id`.
There's another hash type called `flash`. A `flash` hash is cleared with each
request. A controller can use this to send a message that can be displayed to
the user on the next request. Ex. `flash[:notice] = 'Post was successfully created.'`

## Rendering HTML or JSON
The following request will be routed to the same controller as before:
`http://localhost:3000/posts/1.json`. However, it will be rendered using the file:
`.app/views/posts/sho.json.builder` and JSON will be returned to the client.

## Redirects
Rails may also respond using the `redirect_to` method. This method actually
tells the browser to send a new request for a different URL. Ex. `redirect_to
'www.example.com'`

Rails also has shorcuts for URLs. Ex `redirect_to posts_url` will redirect to the
index method in the `PostController`.

You can assign a flash message as a part of a redirection: `redirect_to @post,
notice: 'Post was successfully created.'`.
