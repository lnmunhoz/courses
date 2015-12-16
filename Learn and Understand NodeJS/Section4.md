# Section 3
Modules, Exports and Require

## JavaScript Aside
### First-Class Functions
Everything you can do with other types you can do with functions.
> You can use functions like strings, numbers, etc...

### An Expression
A block of code that results in a value.
> Function expressions are possible in JavaScript because functions are first-class

### Examples
Function Statement:
```js
function greet() {
  console.log('Hi');
}
greet();
```
Functions are First-Class:
```js
function logGreeting(fn){
  fn();
}
logGreeting(greet);
```
Function Expression:
```js
var greetMe = function(){
  console.log('Hi Lucas');
}
greetMe();

// Still first-class
logGreeting(greetMe);
```
