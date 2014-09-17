# Collections, Blocks and Iterators

## Collections
The most important collection classes in Ruby are `Array` and `Hash`. In addition,
a `Set` class was recently added to the language. This classes includes the
`Enumerable` module as a mixin.

### Hash
A Hash is an **associative array** (key-value pairs).

```ruby
phone = {'home' => 1, 'mobile' => 2, 'work' => 3}
```

Or better yet:
```ruby
phone = {:home => 1, :mobile => 2, :work => 3}
```

### Nested Collections
To create a multidimensional collection, just nest one collection inside other.

## Code Blocks
A `block` consists of multiple lines of code, enclosed in curly braces, that can
be passed as a parameter to a method.

```ruby
def three_times
  yield
  yield
  yield
end
```

Then:
```bash
> three_times {puts "Hello"}
```

This will print "Hello" three times.

## Iterators
The `each` method in the `Enumerable` module works something like:

```ruby
def each
  for each item in the collection # pseudocode
    yield(item)
  end
end
```

Example:

```bash
> a = [1, 2, 3]
> a.each {|element| puts element}
# => 1
# => 2
# => 3
```
