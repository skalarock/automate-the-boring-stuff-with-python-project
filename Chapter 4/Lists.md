## Chapter 4: Lists

### The list data type

- A list a value that contains multiple values in ordered sequence which are comma delimited and stored in square brackets.

  ```python
  [1, 2, 3]
  ['hello', 3.1415, True, None, 42]
  spam = ['cat', 'bat', 'rat', 'elephant']
  ```

- To access items in a list, use an integer index for the item's position in the list (starting with 0):

  ```python
  spam = ['cat', 'bat', 'rat', 'elephant']
  spam[0]           # 'cat'
  spam[1]           # 'bat'
  spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
  spam[0][1]        # 'bat'
  ```

- You can also access items in reverse order by using a negative integer with -1 starting as the last item in the list:

  ```python
  spam[0][-1]       # 'rat'
  # An item's value can be reassigned by accessing the index:
  spam[0] = 'mouse'
  spam              # ['mouse', 'elephant']
  ```

#### Getting sublist with slices

- A **slice** can get multiple items in a list by specifying the index at which the slice begins and the index at which the slice ends:

  ```python
  spam = ['cat', 'bat', 'rat', 'elephant']
  spam[0:2]   # ['cat', 'bat']
  # You can redefine multiple items in a list by using a slice:
  spam[1:3] = ['dog', 'fish']
  spam        # ['cat', 'dog', 'fish', 'elephant']
  ```

- you can leave out one or both of the indexes on either side of the colon in the slice:

   ```python
   spam = ['cat', 'bat', 'rat']
   spam[:2]   # ['cat', 'bat']
   ```

- To view the **length** of a list, use the `len()` function:

  ```python
  spam = ['cat', 'bat', 'rat']
  len(spam)   # 3
  ```

- Changing values in a list with indexes

  ```python
  spam = ['cat', 'bat', 'rat']
  spam[1] = 'aardvark'
  spam   # ['cat', 'aardvark', 'rat']
  ```

- To **concatenate** lists, use the `+` or `*` operators:

  ```python
  [1, 2, 3] + [4, 5, 6]   # [1, 2, 3, 4, 5, 6]
  [1, 2, 3] * 3           # [1, 2, 3, 1, 2, 3, 1, 2, 3]
  ```

- To **delete** items from a list, use the `del` statement:

  ```python
  spam = ['cat', 'bat', 'rat', 'elephant']
  del spam[2]
  spam    # ['cat', 'bat', 'elephant'']
  ```

#### Using for loops with lists

- A list can be iterated over in a for loop in the same manner as a `range` object:

  ```python
  # Both loops produce the same output:
  for i in range(4):
      print(i)
  for i in [0, 1, 2, 3]:
      print(i)
  ```

- common Python technique is to use `range(list(somelist))` with a for loop to iterate ver the indexes of a list:

  ```python
  supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
  for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
  
  # Index 0 in supplies is: pens
  ```

#### The in and not in operators

- you can determine whether a value is or is not in a list with the in and not in operators

  ```python
  'howdy' in ['hello', 'hi','howdy','heyas']
  True
  'cat' in spam
  False
  'cat' not in spam
  True
  ```

#### Multiple assignment

- it is a shortcut that lets you assign multiple variables with the values in a list in one line of code

  ```python
  cat = ['fat','black','loud']
  size = cat[0]
  color = cat[1]
  disposition = cat[2]
  size, color, disposition = cat
  ```

### List Methods

- The `index()` method returns the index of the first occurrence of the specified value:

  ```python
  spam = ['hello', 'hi', 'howdy', 'heyas']
  spam.index('hello')    # 0
  spam.index('howdy howdy howdy')   # (Raises an exception if value not found)
  ```

- The `append()` method appends an item to the end of the list:

  ```python
  spam = ['cat', 'dog', 'bat']
  spam.append('moose')
  spam   # ['cat', 'dog', 'bat', 'mooose']
  ```

- The `insert()` method inserts the specified value at the specified position:

  ```python
  spam = ['cat', 'dog', 'bat']
  spam.insert(1, 'chicken')
  spam    # ['cat', 'chicken', 'dog', 'bat']
  ```

- The `remove()` method removes the first occurrence of the item with the specified value:

  ```python
  spam = ['cat', 'bat', 'elephant', 'rat']
  spam.remove('bat')
  spam                  # ['cat', 'elephant', 'rat']
  spam.remove('chicken')    # (Throws an error)
  ```

- The `sort()` method sorts a list in ascending order by default. The sorting direction can be reversed by using the `reverse` keyword argument:

  ```python
  spam = [2, 5, 3.14, 1, -7]
  spam.sort()
  spam    # [-7, 1, 2, 3.14, 5]
  spam = ['ants', 'badgers', 'dogs']
  spam.sort()
  spam    # ['ants', 'badgers', 'cats']
  spam.sort(reverse=True)
  spam    # ['cats', 'badgers', 'ants']
  ```

  - **NOTE:** You cannot sort an array that contains both number and string types.
  - **ALSO:** When working with strings, `sort()` actually sorts by "**ASCII-betical**" order rather than alphabetical order (resulting in uppercase letters being sorted before lowercase letters, because uppercase letters appears before lowercase letters in ASCII code). However, you can sort by true alphabetical order by using the `key` keyword argument:

    ```python
    spam = ['a', 'z', 'A', 'Z']
    spam.sort()
    spam    # ['A', 'Z', 'a', 'z']
    # str.lower is a string method that converts a string input to lowercase:
    spam.sort(key=str.lower)
    spam    # ['A', 'a', 'Z', 'z']
    ```
