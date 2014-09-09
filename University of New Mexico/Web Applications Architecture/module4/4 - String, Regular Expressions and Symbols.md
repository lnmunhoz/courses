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
