# 0x00. Python - Variable Annotations
Learning Objectives
General
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

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

## How to validate your code with mypy
 
