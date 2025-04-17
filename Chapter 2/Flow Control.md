## Chapter 2: Flow Control

#### Booleans

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
