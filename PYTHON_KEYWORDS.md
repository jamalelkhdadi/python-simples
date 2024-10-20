# Keywords

This list contains **reserved keywords** in Python. These are special words that have predefined meanings in the language's syntax and structure. You cannot use these keywords as variable names, function names, or identifiers because they are part of the language's core.

Here's a breakdown of what they represent:


### **Boolean Values:**
- `True`: Represents a true condition.
```python

```
- `False`: Represents a false condition.
```python

```


### **Null Value:**
- `None`: Represents the absence of a value or a null-like object.
```python

```


### **Control Flow Statements:**
- `if`, `elif`, `else`: Used for conditional statements.
```python

```
- `try`, `except`, `finally`: Used for exception handling.
```python
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")
```
- `for`, `while`: Looping structures.
```python

```
- `break`: Exits the closest enclosing loop.
```python

```
- `continue`: Skips the rest of the code in the current loop iteration.
```python
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)
```
- `pass`: Placeholder statement (does nothing).
```python

```


### **Functions and Classes:**
- `def`: Defines a function.
```python

```
- `return`: Returns a value from a function.
```python

```
- `yield`: Used with generators to return a value without terminating the function.
```python
def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"
x = myFunc()
for z in x:
  print(z)
```
- `class`: Defines a class.
```python
class Person:
  name = "John"
  age = 36
pl = Person()
print(pl.name)
```
- `lambda`: Creates anonymous functions (functions without a name).
```python
x = lambda a, b : a * b
print(x(5, 2))
```


### **Exception Handling:**
- `raise`: Raises an exception.
```python
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
```
- `assert`: Used to check if a condition is met, raising an exception if it’s not.
```python
x = "welcome"
#if condition returns False, AssertionError is raised:
assert x != "hello", "x should be 'hello'"
```


### **Asynchronous Programming:**
- `async`: Defines a coroutine function.
```python

```
- `await`: Pauses the execution of a coroutine until the awaited task is completed.
```python

```


### **Logical Operators:**
- `and`, `or`, `not`: Used for logical operations.
```python

```


### **Membership and Identity Operators:**
- `in`: Checks if a value exists within an iterable (like a list or a string).
```python

```
- `is`: Checks if two objects refer to the same instance.
```python

```


### **Scope and Namespace Management:**
- `global`: Declares a global variable inside a function.
```python
def myfunction():
  global x
  x = "hello"
#execute the function:
myfunction()
#x should now be global, and accessible in the global scope.
print(x)
```
- `nonlocal`: Refers to a variable in the nearest enclosing scope that’s not global.
```python
def foo():
    name = "geek" # Our local variable
    def bar():
        nonlocal name          # Reference name in the upper scope
        name = 'GeeksForGeeks' # Overwrite this variable
        print(name)
    # Calling inner function
    bar()
    # Printing local variable
    print(name)
foo()
```


### **Modules and Imports:**
- `import`: Imports a module.
```python

```
- `from`: Imports specific parts of a module.
```python

```
- `as`: Creates an alias for a module or assigns an exception to a variable.
```python

```


### **Context Managers:**
- `with`: Used for resource management (e.g., opening files).
```python

```

### **Object Management:**
- `del`: Deletes an object.
```python
x = ["apple", "banana", "cherry"]
del x[0]
print(x)
```

These keywords are essential to Python's syntax. If you attempt to use them for anything other than their intended purpose, Python will throw a syntax error. 
