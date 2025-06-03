## Practice questions

1. What are the two values of the Boolean data type? How do you write them?

- True and False, needs to start with capital letter

2. What are the three Boolean operators?

- and, or, not

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

  ```python
  # and
  True and True is True.
  True and False is False.
  False and True is False.
  False and False is False.
  # or
  True or True is True.
  True or False is True.
  False or True is True.
  False or False is False.
  # not
  not True is False.
  not False is True.
  ```

4. What do the following expressions evaluate to?
  
  ```python
  (5 > 4) and (3 == 5)                   # False
  not (5 > 4)                            # False
  (5 > 4) or (3 == 5)                    # True
  not ((5 > 4) or (3 == 5))              # False
  (True and True) and (True == False)    # False
  (not False) or (not True)              # True
  ```

5. What are the six comparison operators?

- ==, !=, <, >, <=, >=

6. What is the difference between the equal to operator and the assignment operator?

- == compares two values and evaluates to boolean, and = is operator to assign value to variable

7. Explain what a condition is and where you would use one.

- Condition is an expression in flow control which evaluates to boolean (True/False)

8. Identify the three blocks in this code:

  ```python
  spam = 0
  if spam == 10:
     print('eggs')
     if spam > 5:
         print('bacon')
     else:
         print('ham')
     print('spam')
  print('spam')
  ```

- first block is after first if, and the other two are print bacon and print ham

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
stored in spam, and prints Greetings! if anything else is stored in spam.

  ```python
  if spam == 1:
    print('Hello')
  elif spam == 2:
    print('Howdy')
  else:
    print('Greatings!')
  ```

10. What can you press if your program is stuck in an infinite loop?

- press CTRL-C

11. What is the difference between break and continue?

- break is moving execution outside the loop and continue will move it to beginning of the loop

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

- They are doing the same where the others are more explicit

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

  ```python
  for i in range(1,11):
    print i
  ```

  ```python
  i = 1
  while i <= 10:
    print(i)
    i += 1
  ```

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

- Can be called by spam.bacon()
