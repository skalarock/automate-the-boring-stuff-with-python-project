## Chapter 3: Functions

### Python's Built-In Functions

#### Standard Library

- Python comes with a set of modules called the **[Standard Library](https://docs.python.org/3/library/)**. Each module is a Python program that contains a related group of functions you can use in your programs (e.g., numeric and mathematical modules). Before you can use the functions in a module, you must **import** the module with an `import` statement:

  ```python
  # Returns a random integer from 1 to 10:

  import random

  random.randint(1, 10)
  ```

- You can specify **multiple** modules for import by separating their names with **commas**:

  ```python
  import random, sys, os, math
  ```

- It is generally considered best to use the syntax outlined above when using a function in a Standard Library module. However, if you want to import and call a function **directly** without needing to reference the module name each time, use the `from` form of an import statement:

  ```python
  # Imports all functions from the "random" module, not the module itself:

  from random import *

  randint(1, 10)
  ```

#### Third-Party Modules

- Modules can be installed by using the `pip` (or `pip3`) tool from the terminal:

  ```shell
  pip install ${MODULE_NAME}
  ```

  - **NOTE:** See [here](http://automatetheboringstuff.com/appendixa/) for more information on installing third-party modules.

### Writing Your Own Functions

- Define a function by using the `def` keyword:

  ```python
  def hello(name):
      print('Hello, ' + name)

  hello('Alice')      # "Hello, Alice"
  ```

- All function calls return a value. You can specify what value should be returned by the function by using a `return` statement:

  ```python
  def plusOne(number):
      return number + 1

  newNumber = plusOne(5)

  print(newNumber)    # 6
  ```

  - **NOTE:** If the value returned is considered "empty" (or if the return statement is omitted entirely), Python still returns a value called `None` (i.e., a value that represents a lack of a value). The `None` value will not be visibly displayed in the console.

- Some functions accept **keyword arguments**, which are used as optional arguments to pass to a function call. For example, the `print()` function adds a newline character by default to the end of the string it prints. However, this behavior can be modified by changing the value of the `end` keyword argument:

  ```python
  # Prints "Hello" and "World" on two separate lines:

  print('Hello')
  print('World')

  # Prints "Hello World" on one line:

  print('Hello', end=' ')
  print('World')
  ```

  - **NOTE:** The `print()` function also contains a `sep` keyword argument that specifies what character should be used to separate multiple arguments (an empty space by default):

    ```python
    # Prints 'cat dog mouse':

    print('cat', 'dog', 'mouse')

    # Prints 'cat, dog, mouse':

    print('cat', 'dog', 'mouse', sep=', ')
    ```

### Global and Local Scopes

- Variables inside of a function can have the same name as variables outside of the function, but they are considered two separate variables due to scope. Variables defined in a function belong to that function's **local scope**, whereas all variables defined outside of functions belong to the application's **global scope**:

  ```python
  spam = 42       # Global variable

  def eggs():
      spam = 42   # Local variable
  ```

- Key Points:

  **1**\.  Code in the global scope cannot use any local variables.

  **2**\.  Code in a local scope can access global variables.

  **3**\.  Code in one function's local scope cannot use variables in another local scope.

  **4**\.  You can use the same name for different variables if they are in different scopes.

- If you want to reassign the value of a global variable (e.g. `eggs = 42`) from within a local scope, you cannot simply say `eggs = 'Hello'`, as this will merely create a local variable named "eggs" within the local scope. Rather, you must use a `global` statement:

  ```python
  eggs = 42

  def spam():
      global eggs
      eggs = 'Hello'    # Overwrites 42 in global "eggs" variable
      print(eggs)       # Prints 'Hello'

  spam()

  print(eggs)           # Prints 'Hello'
  ```
