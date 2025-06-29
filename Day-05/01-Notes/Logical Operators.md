# Logical Operations in Python

## Introduction

Logical operators in Python are used to manipulate and combine Boolean values. These operators allow you to perform logical operations such as AND, OR, and NOT.

## List of Logical Operators

1. **AND (and):** Returns `True` if both operands are `True`.
2. **OR (or):** Returns `True` if at least one of the operands is `True`.
3. **NOT (not):** Returns the opposite Boolean value of the operand.

## Examples

### AND Operator

```python
x = True
y = False
result = x and y
# result will be False
```

### OR Operator

```python
a = True
b = False
result = a or b
# result will be True
```
Great! Here's the full overview of logical operators in Python:

---

### ✅ **1. `and` Operator – Returns `True` only if both are `True`**

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

### ✅ **2. `or` Operator – Returns `True` if **at least one** is `True`**

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

### ✅ **3. `not` Operator – Reverses the Boolean value**

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

### 🔎 Examples in Python:

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
print(not False)        # True
```

---

Let me know if you want these with real-world examples too (like in conditions or if statements).
