# The Blog App - Iteration 3 (Validations)

Data validation is the oricess of ensuring your web application operates
on clean, correct and useful data. The most common web applications security
weakness is failure to validate client-side input.

#### Most common attacks:
- SQL injection
- Cross-site scripting
- Bugger overflow

## Data Validations
 Where they can happen?
- JavaScript, HTML
- Controller-level, Modell-level
- Database - Stored Procedure

### Client-side
Involves checking HTML forms.
- JavaScript
- HTML5

### Server-side
Checks made after an HTML form has been submitted.
- Database (stored procedures)
- Controller-level (not recommended)
- Model-level (recommended)

## ActiveRecord Callbacks

`ActiveRecord` objects have methods that can be called in order to ensure their
integrity at the various stages of their lifecycle.

### Callbacks
Are methods that get called at certain points in an `ActiveRecord` object's
lifecycle. They are "hooks" into the  lifecycle, allowing you to trigger logic
before or after the state of an object changes.

## ActiveRecord Validations
Validations are a type of `ActiveRecord` callback that can be used to ensure
only valid data is stored in your Rails databases. They are defined in your models.

```ruby
class Person < ActiveRecord::Base
  validates_presence_of :name
  validates_numericality_of :age, only_integer => true
  validates_confirmation_of :email
  validates_length_of :password, :in => 8..20
end
```
