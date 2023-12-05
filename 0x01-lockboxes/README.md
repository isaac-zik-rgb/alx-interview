# 0x01-lockboxes
THIS DIRECTORY CONTAINS A PYTHON FILE THAT FINDS IF ALL BOXES CAN BE OPENED
* 0-lockboxes.py: <br/>
Function that determines if all the boxes can be opened.
  * Prototype: def canUnlockAll(boxes)
  * Return: True if all boxes can be opened, else return False
  * boxes is a list of lists
  * A key with the same number as a box opens that box
  * The first box boxes[0] is unlocked
  * All keys can be assumed to be positive integers
  * There can be keys that do not have boxes
  * The first box boxes[0] is unlocked
  * All boxes can be assumed to be unique and will have at least one key
  * The function should allow to find keys recursively
  * A [list](/rltoken/6X6Z3Q8ZQ8QX6ZQX6ZQX6ZQ) is used to keep track of the keys found
  * A [list](/rltoken/6X6Z3Q8ZQ8QX6ZQX6ZQX6ZQ) is used to keep track of the boxes opened
  * The code is not allowed to import any module
  * You are allowed to use [print](/rltoken/6X6Z3Q8ZQ8QX6ZQX6ZQX6ZQ)
``  
yosri@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll
