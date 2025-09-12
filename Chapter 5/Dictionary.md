## Chapter 5: Dictionaries and structuring data

### The dictionary data type

- A dictionary is a collection of many values, indexes are called keys, and key with its value is called key-value pair

  ```python
  myCat = {'size': 'fat', 'color' : 'gray', 'disposition' : 'loud'}
  myCat['size']
  'fat'
  'My cat has ' + myCat['color'] + ' fur.'
  'My cat has grey fur.'
  ```

  - Two dictionaries with identical key-value pairs will be considered equivalent regardless of the order in which those key-value pairs are arranged:

  ```python
  eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
  ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}

  eggs == ham   # True
  ```

#### keys(), values(), items()

- There are three dictionary methods that will return list-like values of the dictionary’s keys, values, or both keys and values: `keys()`, `values()`, and `items()`

  ```python
  myCat = {'size': 'fat', 'color' : 'gray', 'disposition' : 'loud'}
  list(myCat.keys())
  ['size', 'color', 'disposition']
  list(myCat.values())
  ['fat', 'gray', 'loud']
  # Tuples are the same as lists, expect they use parentheses (not brackets)
  list(myCat.items())
  [('size', 'fat'), ('color', 'gray'), ('disposition', 'loud')]
  # Check if a key exists with the "in" and "not in" operators:
  'name' in myCat       # False
  'name' not in myCat   # True
  ```

- You can iterate over a dictionary's keys/values with a for loop:

  ```python
  eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
  for k in eggs.keys():
      print(k)
  # Prints 'name', 'species', and 'age'
  for k, v in eggs.items():
      print(k + ': ' + str(v))
  # Prints 'name: Zophie', 'species: cat', and 'age: 8'
  ```

- Dictionaries have a `get()` method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist

  ```python
  picnicItems = {'apples': 5, 'cups': 2}
  'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
  'I am bringing 2 cups.'
  'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
  c'I am bringing 0 eggs.'
  ```

- If you want to set a value for a key that does not yet exist in a dictionary, use the `setdefault()` method:

  ```python
  spam = {'name': 'Pooka', 'age': 5}
  spam.setdefault('color', 'black')
  spam
  {'color': 'black', 'age': 5, 'name': 'Pooka'}
  ```

#### Pretty printing

- If you import the pprint module into your programs, you will have access to the `pprint()` and `pformat()`

  ```python
  import pprint
  message = 'It was a bright cold day in April, and the clocks were striking
  thirteen.'
  count = {}
  for character in message:
     count.setdefault(character, 0)
     count[character] = count[character] + 1
  pprint.pprint(count)
  ```

- If you want to obtain the prettified text as a string value instead of displaying it on the screen, call `pprint.pformat()` instead

### Using data structures

- You can model things with data structures in whatever way you like, as long as the rest of the code in your program can work with the data model correctly. When you first begin programming, don’t worry so much about the “right” way to model data. As you gain more experience, you may come up with more efficient models, but the important thing is that the data model works for your program’s needs.
