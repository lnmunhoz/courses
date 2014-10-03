# Strings, Regular Expressions and Symbols

## Strings

You can insert arbitrary Ruby expressions using string interpolation.

```bash
> "360 degrees=#{2*Math::PI} radians"
=>"360 degrees6.283185307179586 radians"
```

If you enclose a string on single **backquotes**, the string will be executed.
```bash
> `date`
=> "Tue Sep 9 18:35:10 MDT 2014\n"
```

The `String` class contains a number of methods which can be used to manipulate
strings.

```bash
> name = "Homer Blinpson" #=> "Homer Blimpson"
> name.length #=> 14
> name[6] #=> "B"
> name[6..14] #=> "Blimpson"
> name.enconding # => #<Enconding:UTF-8>
```

# Regular Expresion Class

Ruby has a **regular expression** class called `Regexp`. In Ruby, a regular
expression is written in the form of: `/pattern/modifiers` where pattern is the
regular expression itself and modifiers are a series of characters indicating
various options.

To test if a particular Regex matches (part of) a string, use the `=~` operator.
This operator returns the character position in the string of the start of the
match, or nil if no match was found.

# Symbols

Symbols has unique space stored in memory, and just once. If the identity of the
object is important, use a symbol.
