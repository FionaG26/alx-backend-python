# 0x00. Python - Variable Annotations
## Learning Objectives

## Type annotations in Python 3
In Python 3, you can use type annotations to specify the types of variables, function parameters, and function return values. Type annotations are a way to provide hints to static type checkers and IDEs about the expected types in your code. They don't affect the runtime behavior of your program but can help catch potential type-related errors early.

## What Are Type Annotations?
Type annotations — also known as type signatures — are used to indicate the datatypes of variables and input/outputs of functions and methods.

## Static vs Dynamic
There are names for these approaches in programming languages. C requires that we explicitly define types — it is a statically typed language.

Python on the other hand, with its more gung-ho approach to variable assignments, is a dynamically typed language.

## How do we define these two approaches?

### Static typed — performs type checking at compile-time and requires datatype declarations.
### Dynamic typed — performs type checking at runtime and does not require datatype declarations.

There are pros and cons to both approaches, but one strength of statically typed languages (which applies to us) is that it makes code very explicit.1. Datatypes are clearly defined in the code, removing any potential datatype ambiguity.
2. Minor typos and errors when writing code can be easier to identify.

## What is Duck Typing in Python?
Duck Typing is a term commonly related to dynamically typed programming languages and polymorphism. The idea behind this principle is that the code itself does not care about whether an object is a duck, but instead it does only care about whether it quacks.Duck Typing refers to the principle of not constraining or binding the code to specific data types.

## Understanding Duck Typing in Python
Let’s consider the + Python operator; If we use it with two integers, then the result will be sum of the two numbers.

>>> a = 10 + 15
>>> a
25
Now let’s consider the same operator with string object types. The result will be the concatenation of the two objects being added together.

>>> a = 'A' + 'B'
>>> a
'AB'
This polymorphic behaviour is a core idea behind Python which is also a dynamically typed language. This means that it performs type checking at run-time as opposed to statically typed languages (such as Java) that perform it during compile-time.

# alx-backend-python - Python Variable Annotations

This repository contains solutions for the Python Variable Annotations project. Each task focuses on different aspects of type annotations in Python.

## Tasks
1. Basic annotations - concat: Implement a type-annotated function concat that concatenates two strings and returns the result.

2. Basic annotations - floor: Implement a type-annotated function floor that takes a float as input and returns its floor value.

3. Basic annotations - to string: Implement a type-annotated function to_str that converts a float to its string representation.

4. Define variables: Define and annotate variables with specific values.

5. Complex types - list of floats: Implement a type-annotated function sum_list that takes a list of floats as input and returns their sum.

6. Complex types - mixed list: Implement a type-annotated function sum_mixed_list that takes a list of integers and floats as input and returns their sum.

7. Complex types - string and int/float to tuple: Implement a type-annotated function to_kv that takes a string k and an int or float v as input and returns a tuple.

8. Complex types - functions: Implement a type-annotated function make_multiplier that takes a float multiplier as input and returns a function that multiplies a float by the given multiplier.

9. Let's duck type an iterable object: Implement a type-annotated function element_length that takes an iterable object as input and returns a list of tuples containing the element and its length.

10. Duck typing - first element of a sequence: Implement a type-annotated function safe_first_element that takes a sequence as input and returns its first element.

11. More involved type annotations: Implement a type-annotated function safely_get_value that retrieves a value from a dictionary given a key and a default value.

12. Type Checking: Implement a type-annotated function zoom_array that zooms in an array by repeating its elements.

### Running the Code
All code files in this repository should follow the Pycodestyle style (version 2.5) to ensure consistent and readable code. To check the code against the Pycodestyle style, use the following command:

pycodestyle <filename.py>
For example, to check the style of the 1-concat.py file, use the command:

pycodestyle 1-concat.py
To validate the type annotations and check for type errors, you can use Mypy. Run Mypy with the following command:

mypy <filename.py>
For example, to run Mypy on the 1-concat.py file, use the command:

mypy 1-concat.py
Ensure that both Pycodestyle and Mypy are installed on your system before running the commands.

Running the Code
To run any of the code files in this repository, ensure that you have Python 3.x installed on your system. Use the following command format to execute the files:

python <filename.py>
For example, to run the 1-concat.py file, use the command:

python 1-concat.py
Make sure the file has executable permissions before running it.

### Style Guide and Documentation
All code files in this repository should follow the Pycodestyle style (version 2.5) to ensure consistent and readable code.

Each module, class, and function should be documented with meaningful docstrings. The purpose and functionality of the code should be clearly explained in sentences.
