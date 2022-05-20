# Dictionary-Implementation-Using-Red-Black-Tree
## Table of Content
- [Dictionary-Implementation-using-Red-Black-Tree](#dictionary-implementation-using-red-black-tree)
  * [Abstract](#abstract)
  * [Functionality](#functionality)
  * [Tools](#tools)
  * [Contributors](#contributors)

## Abstract
Most of the Binary Search Tree operation (e.g., search, max, min, insert) take O(h) time where h is the height of the BST. In the best case, the height of a BST is equal to log n, however, since it does not balance itself it can become degenerate(skewed) which may lead us to the worst case where height is equal to n.

A red-black tree is a self-balancing BST. It has the advantage of ensuring a worst case of O(log n) time complexity at all times whereas a BST may become degenerate (skewed) and require O(n).

This implementation contains all the red-black tree operations except remove. 

 ## Functionality
**This program lets you:** 
1. Load dictionary from text file into a red-black tree
2. Print the number of words present in the dictionary
3. Insert a word
4. Check if a word exists in the dictionary or not
5. Print the height of the tree 
6. Print the black height of the tree
7. Includes a method to print the whole tree in datastructure.py (wasn't added to main menu as the tree will be too big since the dictionary contains over 90k words) 
## Tools
1. IntelliJ PyCharm (IDE)
2. Python 3
## Contributors
1. [Adham Mohamed](https://github.com/adhammohamed1)
2. [Yousef Kotp](https://github.com/yousefkotp)
3. [Mohamed Farid](https://github.com/MohamedFarid612)
