# Lists
- Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.
- Operations you can perform on lists: 
    - append : add element in the end of the list 
    - delete : delete any specified element from the list 
    - len : count the number of elements in the list
    - insert : can add a new element at any place in the list, not only at the end

## Negative Indices in Lists 
- It may look strange, but negative indices are legal, and can be very useful.
- An element with an index equal to `-1` is the last one in the list.
- An element with an index equal to `-2` is the one before last in the list.
- [Refer q4.py](./q4.py)


## Swap in python

- This is the traditional method you can use : 

![alt text](image.png)

- Python offers a more convenient way of doing the swap – take a look:

![alt text](image-1.png)

- you can easily swap the list's elements to reverse their order:

![alt text](image-2.png)


## referencing in python 

- When you assign one list to another, such as list_2 = list_1, you are not creating a new copy of the list. Instead, you are creating a **new reference** to the same list in memory. 

![alt text](image-3.png)

## Powerful slices 

- A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
- It actually copies the list's contents, not the list's name.

![alt text](image-4.png)

- This inconspicuous part of the code described as [:] is able to produce a brand new list.
- [refer q8.py](./q8.py)


One of the most general forms of the slice looks as follows:

![alt text](image-5.png)

[refer q9.py](./q9.py)


### Negative slices 

![alt text](image-6.png)
![alt text](image-7.png)

### delete in slices 

![alt text](image-8.png)
![alt text](image-9.png)

Deleting all the elements at once is possible too:

![alt text](image-10.png)

Removing the slice from the code changes its meaning dramatically. Take a look: 

![alt text](image-11.png)
![alt text](image-12.png)


## `in` and `not in` operators 

- Python offers two very powerful operators, able to look through the list in order to check whether a specific value is stored inside the list or not.

![alt text](image-13.png)
![alt text](image-14.png)

## some examples of lists

- [refer q14.py](./q14.py)