## Chapter 6: Manipulating strings

### Working with strings

- There are multiple ways to type strings with double quotes or escape chars:

  ```python
  spam = "That is Alice's cat."
  spam = 'Say hi to Bob\'s mother.'
  print("Hello there!\nHow are you?\nI\'m doing fine.")
  ```

- Types of escape characters:

| Escape character | Prints as            |
| :--------------: | -------------------- |
| \\'               | Single quote         |
| \\"               | Double quote         |
| \t               | Tab                  |
| \n               | Newline (line break) |
| \\              | Backslash            |

- raw string completely ignores all escape characters and print any backslash that appears in the string

  ```python
  print(r'That is Carol\'s cat.')
  That is Carol\'s cat.
  ```

- A multiline string in Python begins and ends with either three single quotes or three double quotes, multiline comments use double quotes

  ```python
  print('''Dear Alice,
  Eve's cat has been arrested for catnapping, cat burglary, and extortion.
  Sincerely,
  Bob''')

  """This is a test Python program.
  Written by Al Sweigart al@inventwithpython.com
  This program was designed for Python 3, not Python 2.
  """  
  ```

#### Indexing and slicing strings

- strings use indexes and slices the same way lists do

  ```python
  spam = 'Hello world!'
  spam[0]
  'H'
  spam[-1]
  '!'
  """  

- in and not in operators can be used with strings just like with lists

  ```python
  'Hello' in 'Hello'
  True
  'HELLO' in 'Hello World'
  False
  """

### Useful strings methods

#### upper(), lower(), isupper(), islower()

- The `upper()` and `lower()` methods return a string where all characters are in uppercase or lowercase, respectively:

  ```python
  spam = 'Hello, world!'
  spam.upper()
  'HELLO, WORLD!'
  spam.lower()
  'hello, world!'
  ```

- **NOTE:** Because strings are immutable, string methods do not modify the original string. If you want to actually modify the string value stored to a variable, you must say, e.g.: `spam = spam.lower()`

- The `isupper()` and `islower()` methods return a Boolean value indicating whether all letters in the string are uppercase or lowercase, respectively:

  ```python
  spam = 'hello, world!'
  spam.isupper()
  False
  spam.islower()
  True
  ```

#### The isX string methods

- These methods return a Boolean value that describes the nature of the string

  ```python
  isalpha()     # (Letters only)
  isalnum()     # (Letters and numbers only)
  isdecimal()   # (Numbers only)
  isspace()     # (Whitespace only)
  istitle()     # (Titlecase only)
  ```

- The `startswith()` and `endswith()` methods return a Boolean value indicating whether the string starts with or ends with (respectively) the specified value:

  ```python
  spam = 'Hello, world!'
  spam.startswith('Hello')
  True
  spam.endswith('!')
  True
  spam.endswith('world')
  False

- The `join()` method takes all items in an iterable and joins them into one string using a specified separator:

  ```python
  spam = ['cats', 'rats', 'bats']
  ', '.join(spam)
  'cats, rats, bats'
  '\n'.join(spam)  # (Inserts newline character after each item)
  ```

- The `split()` method splits a string into a list. The method splits a string according to whitespace separation by default. However, you can specify the string to be used as the separator (first parameter) and the number of splits to perform (second parameter):

  ```python
  spam = 'My name is Simon'
  spam.split()       
  ['My', 'name', 'is', 'Simon']
  spam.split('m')    
  ['My na', 'e is Si', 'on']
  ```

- The `ljust()` and `rjust()` methods return a "padded" version of a string with a number of spaces (first parameter) inserted to left or right justify (respectively) the specified text. An optional second parameter can be used to specify a padding character other than a space. There is also a `center()` method that operates similarly to `ljust()` and `rjust()` but uses padding to center the text, rather than justify left or right:

  ```python
  'Hello'.ljust(10)        
  'Hello     '
  'Hello'.rjust(10)        
  '     Hello'
  'Hello'.ljust(10, '.')   
  'Hello.....'
  'Hello'.center(15, '-')  
  '-----Hello-----'
  ```

- Use the `strip()`, `rstrip()`, and `lstrip()` methods to trim whitespace characters off of a string. You can insert a string as an argument, and any contiguous set of characters in that argument (regardless of order) will be stripped from the end(s) of the string:

  ```python
  spam = '  Hello World  '
  spam.strip()
  'Hello World'
  spam.lstrip()
  'Hello World  '
  spam.rstrip()
  '  Hello World'
  'SpamBaconSpamEggsSpam'.strip('ampS')
  'BaconSpamEggs'
  ```

- `pyperclip` has `copy()` and `paste()` functions that can send text to and receive text from computer clipboard

  ```python
  import pyperclip
  pyperclip.copy('Hello World')
  pyterclip.paste()
  'Hello world'
  ```
