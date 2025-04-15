## Chapter 1: Python Basics

### Basic Terminology and Using IDLE

Run Python IDLE or other IDEs you are used to and enter expressions in examples in interactive shell.

#### Expressions

- Expressions consist of values (such as 2) and operators (such as +), and they can always evaluate (that is, reduce) down to a single value. (including combinations of numbers and strings):

- Expressions are just values combined with operators, and they alway evaluate down to single value. Data type is a category for values (Integer, Floats, Strings, ...)

  ```python
  2 + 2                 # 4

  'Alice' + 'Bob'       # 'AliceBob'

  'Alice' * 5           # 'AliceAliceAliceAliceAlice'

  'Alice' + 42          # trying to concatenate an integer to the string
  Traceback (most recent call last):
    File "<pyshell#26>", line 1, in <module>
       'Alice' + 42
  TypeError: Can't convert 'int' object to str implicitly
  ```

#### Storing values in variables

- storing values in variables with and assignment statement (variable name, equal sign and value)

- Declaring a variable:

  ```python
  spam = 'Hello'
  spam                   # Hello
  spam = 'Goodbye'
  spam                   # Goodbye
  ```

Variable names:

- It can be only one word
- It can use only letters, numbers and the underscore
- It can't begin with a number
- Python convention to start your variables with a lowercase letter

### Writing Our First Program

- Create a file named `Hello.py` containing the following code:

  ```python
  # This program says hello and asks for your name:

  print('Hello world!') 
  print('What is your name?')
  myName = input()
  print('It is good to meet you, ' + myName)
  print('The length of your name is:')
  print(len(myName))
  print('What is your age?')
  myAge = input()
  print('You will be ' + str(int(myAge) + 1) + ' in a year.')
  ```
  
  - Hash mark (`#`) is used to comment, and those are ignored by Python, you can use them for notes, etc

  - `print()` displays the string value inside the parentheses on the screen

  - `input()` accepts the value of the user's keyboard input and returns a **string** value.

    - **NOTE:** The program will wait until the input is entered before continuing to execute the remaining code.

  - `len()` takes a string argument and evaluates to the integer value of the number of characters in that string:

    ```python
    len('Al')   # 2
    ```

  - `str()` function can be passed an integer value and will evaluate to a string
value version of it:

    ```python
    str(42)     # '42'
    ```

  - `int()` function takes an argument and converts it into an integer data type:

    ```python
    int('42')    # 42
    ```

    - **NOTE:** If you want to convert to a **floating point** number (i.e., a number with a decimal point) use `float()`:

      ```python
      float('3.14')   # 3.14
      ```

- **NOTE:** On Linux distro or OS X, you may need to run `python3` rather than `python` to run the current version of Python.
