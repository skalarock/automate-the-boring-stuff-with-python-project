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

- you can leave out one or both of the indexes on either side
of the colon in the slice

   ```python
   spam = ['cat', 'bat', 'rat']
   spam[:2]   # ['cat', 'bat']
   ```

- To view the **length** of a list, use the `len()` function:

  ```python
  spam = ['cat', 'bat', 'rat']

  len(spam)   # 3
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
