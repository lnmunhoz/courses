# Classes and Inheritance

Classes are defined using the keyword `class` followed by the name of the class.
They must begin with a Capital, and the convention is CamelCase.

```ruby
class MyCLass
  @boo # an instance variable
  def my_method
    @foo = 2 # an instance variable
  end
end
```

## Methods

An instance variable can only be directly accessed or modified within a method
definition.
```ruby
class MyCLass
  def boo
    return boo
  end
  def boo=(val)
    @boo = val
  end
end
```

Ruby methods have implicit return values. The value of the last expression
executed in a method is its return value.

The return statement still exists, but is not required.

```ruby
def min(x, y)
  if x < y then x else y end
end
```

- When invoking a method, parentheses are optional.
- If the method ends with a question mark it indicates that the return value
is boolean.
- If the method ends with an exclamation, it indicates that the method can
change the state of the object.
- By default, every method in a class is `public`, and every istance variable
is `protected`.



## Class methods
Class methods are created in the same way as normal methods, except they are
prefixed by the keyword `self`.

```ruby
class MyClass
  def self.cls_method
    "MyClass type"
  end
end
```

## Inheritance, Mixins and Extending Classes

- Only single inheritance is supported.
- Classes are never closed, its always possible add methods to an existing class.

The syntax for inheritance

```ruby
class MyClass < SuperClass
  ...
end
```

- Its possible to create its own namespace by using the keyword `module`.
- To include the module, use the keyword `require`.
- Use the `include` keyword to create mixins.

## Accessors

There is a shorthand way of providing accessors for an object's attributes.

```ruby
class MyClass
  attr_accessor :boo
end
```

If just a getter or setter is needed, we can use `attr_reader` or `attr_writer`.
