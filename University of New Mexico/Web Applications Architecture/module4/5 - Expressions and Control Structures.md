# Expressions and Control Structures

Ruby syntax is expression-oriented. **Everything** in Ruby is treated as an
expression and therefore evaluates to something.

## Conditional Execution

The most basic syntax for expression conditionals:
```ruby
if expression
  code
end
```
Where *code* is executed if and only if the conditional expression evaluates
to something different than `false` or `nil`.

Example of else clauses:
```ruby
if expression1
  code
elsif expression2
  code
else
  code
end
```

Shorthand way of expressing `if`:
```ruby
code if expression
```

Ruby also has the ternary operator `?:`.

### Comparison operators:
- `--`: Equals
- `!=`: Different
- `=~`: Matches with a regular expression
- `!~`: Don't match with a regular expression
- `===` Used in `case` statements (case equality operator)

### Syntactic Sugar

The following code is the opposite of an `if` statement:
```ruby
until expression
  code
end
```
You cannot attach `else` clauses to the `until` condition.

## Iteration

The `for/in` loop:
```ruby
for var in collection do
  body
end
```

Exit condition loop:
```ruby
while condition do
  body
end
```

Exit condition loop, opposite of while:
```ruby
until condition do
  body
end
```
