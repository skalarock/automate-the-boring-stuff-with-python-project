## Chapter 2: Flow Control

### Booleans

- Booleans have two values: `True` and `False` (Boolean is capitalized because the data type is named after mathematician George Boole.).

#### Comparison Operators

- Overview:

  | Operator | Meaning                  |
  | :------: | ------------------------ |
  |    ==    | Equal to                 |
  |    !=    | Not equal to             |
  |    <     | Less than                |
  |    >     | Greater than             |
  |    <=    | Less than or equal to    |
  |    >=    | Greater than or equal to |

- Expressions with comparison operators evaluate to a Boolean value:

  ```python
  42 == 42      # True

  42 >= 99     # False

  2 != 3       # True

  2 != 2       # False
  ```

#### Boolean Operators

- Overview:

  ```python
  # The "and" operator returns true when all values are true:

  True and True     # True
  True and False    # False
  False and True    # False
  False and False   # False

  # The "or" operator returns true when at least one value is true:
  
  True or True      # True
  True or False     # True
  False or True     # True
  False or False    # False

  # The "not" operator evaluates to the opposite Boolean value:
  
  not True          # False
  not False         # True

  ```

- Example of mixing operators:

  ```python
   2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2   # True
  ```

### Elements of flow control

- start with a part called the condition, and all are followed by a block of code called the clause.

#### Conditions

- always evaluate to True or False and flow control decides what to do based on this

#### Blocks of code

 1. Blocks begin when the indentation increases.
 2. Blocks can contain other blocks.
 3. Blocks end when the indentation decreases to zero or to a containing block’s indentation

### Flow control statements

#### if statement

- The if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. The clause is skipped if the condition is False.

  ```python
  if name == 'Alice':
      print('Hi, Alice.')
  ```

#### else statement

- The else clause is executed only when the if statement’s condition is False.

  ```python
  if name == 'Alice':
      print('Hi, Alice.')
  else:
    print('Hello, Stranger.')
  ```

#### elif statement

- The elif statement is an “else if” statement that always follows an if or another elif statement.

  ```python
  if name == 'Alice':
      print('Hi, Alice.')
  elif age < 12:
    print('You are not Alice, kiddo.')
  elif age > 100:
    print('You are not Alice, grannie.')
  ```

#### while loop statement

- You can make a block of code execute over and over again with a while statement.
- The code in a while clause will be executed as long as the while statement’s condition is True.

  ```python
  spam = 0
  if spam < 5:
    print('Hello, world')
    spam = spam + 1
  ```
