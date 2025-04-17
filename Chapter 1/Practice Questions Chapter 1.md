## Practice questions

1. Which of the following are operators, and which are values?

  ```python
  *                  # Operator
  'hello'            # Value
  -88.8              # Value
  -                  # Operator
  /                  # Operator
  +                  # Operator
  5                  # Value
  ```

2. Which of following is a variable, and which is a string?

  ```python
  spam               # Variable
  'spam'             # String
  ```

3. Name three data types

- integer
- string
- floating-point numbers

4. What is an expression made up of? What do all expressions do?

- Expression is combination of values and operators
- Expressions evaluate to a single value

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

- An expression evaluates to a single value and statement does not.

6. What does the variable bacon contain after the following code runs

  ```python
  bacon = 20
  bacon + 1
  ```

- The result is 21, however the value of bacon is not re-assigned and is still 20

7. What should the following two expressions evaluate to?

 ```python
 'spam' + 'spamspam'
 'spam' * 3
 ```

- both are sting 'spamspamspam'

8. Why is eggs a valid variable name while 100 is invalid?

- variable names cannot begin with a number

9. What three functions can be used to get the integer, floating-point number, or string version of a value?

- int(), str(), float()

10. Why does this expression cause an error? How can you fix it?

 ```python
 'I have eaten ' + 99 + ' burritos.'
 ```

- expression is failing as 99 is int and not string, it can be corrected by using str(99) instead

Extra credit: Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell

The len() function [python documentation](https://docs.python.org/3/library/functions.html#len)
