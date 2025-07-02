## Practice questions

1. What is []?

- empty list

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].) For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

  ```python
  spam[2]= 'hello'
  ```

3. What does spam[int(int('3' * 2) / 11)] evaluate to?

- 3

4. What does spam[-1] evaluate to?

- negative indexes count from the end

5. What does spam[:2] evaluate to? For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

- [3.14, 'cat']

6. What does bacon.index('cat') evaluate to?

- 1

7. What does bacon.append(99) make the list value in bacon look like?

- [3.14, 'cat', 11, 'cat', True, 99]

8. What does bacon.remove('cat') make the list value in bacon look like?

- [3.14, 11, 'cat', True]

9. What are the operators for list concatenation and list replication?

- list concatenation is +, list replication is *

10. What is the difference between the append() and insert() list methods?

- append() is adding only on the end of the list, while insert() can add them anywhere

11. What are two ways to remove values from a list?

- del or remove()

12. Name a few ways that list values are similar to string values.

- strings and list can be passed to len(), can be used for loops

13. What is the difference between lists and tuples?

- lists are mutable (), tuples are immutable []

14. How do you type the tuple value that has just the integer value 42 in it?

- (42,)

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

- tuple(), list()

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

- contain reference to the list values

17. What is the difference between copy.copy() and copy.deepcopy()?

- copy.copy() full do shallow copy of a list, while the copy.deepcopy() will do a deep copy of a list
