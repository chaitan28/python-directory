### 🔹 What Are Functions in Python?

**Functions** in Python are **reusable blocks of code** that perform a specific task.
They help you avoid repetition and make your code modular and organized.

---

### ✅ Syntax:

```python
def function_name(parameters):
    # code block
    return result
```

### 🔸 Example : Simple Function

```python
def greet(): print("Hello, Chaitanya!")

greet()  # calling the function
```
---

### ✅ 1. **Built-in Functions**

* Provided by Python.
* Examples: `print()`, `len()`, `type()`, `sum()`, `input()`

```python
print("Hello")     # built-in function
length = len("abc")
```
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

### ✅ 2. **User-defined Functions**

* Created by the programmer using the `def` keyword.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Chaitanya")
```

---

### ✅ 3. **Lambda Functions** (Anonymous Functions)

* Small, single-line functions using the `lambda` keyword.

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

### ✅ 4. **Recursive Functions**

* A function that calls itself.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### ✅ 5. **Built-in Higher-order Functions**

* Take other functions as arguments.
* Examples: `map()`, `filter()`, `reduce()`, `sorted()` with `key`

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]
```
