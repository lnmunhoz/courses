# Objects and Variables

**Everything in Ruby is an object.** The `Object` class is the parent class of
all classes in Ruby.

## Object

An important method in the `Object` class is `class()`. It returns the "type" of
an object.

```ruby
> 1.class()   # => Fixnum

```

Or without the parenthesis.

```ruby
> 1.class     # => Fixnum

```

## Variables

Ruby does not use variable declarations. If you assign a value to a literal, an
"appropriate" variable named after that literal is created.

A variable just holds a reference to an object, and does not care about the type
of the object.

### Conventions

Ruby uses simple naming conventions to denote the scope of variables.
- `name` could be a local variable.
- `@name` an instance variable.
- `@@name` a class variable.
- `$Name` a global variable

**Local variables** must begin with a lowercase letter, and the convention is to use
underscores, rather than camel case, for multi-word names.

**Constants** are any name that starts with  an uppercase letter, and the convention
is to use underscores.

**Classes** and **modules** are treated as constants, so they begin with uppercase
letters, and the convention is to use camel case.
