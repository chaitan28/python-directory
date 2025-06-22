# def fun_name(parameters): 
     # fun_body
# calling the function: fun_name(arguments) 


### **1. First Function – Uses `print()` Inside the Function**

```python
def add(a, b): 
    c = a + b
    print(c)

add(2, 3)

```

#### ✅ **What It Does:**

* Accepts 2 numbers (`a`, `b`).
* Adds them and stores the result in `c`.
* Prints `c` **inside** the function using `print(c)`.

#### ⛔ **What It Does NOT Do:**

* It **does not return** the result. So if you try to store or reuse the result, you **can’t**.

#### 🔍 **Result:**

```python
Output: 5
```



### 🔹**2. Second Function – Uses `return`**

```python
def add(f, e, h):
    k = f + e + h   # k is variable
    return k

print(add(2, 4, 5))
```

#### ✅ **What It Does:**

* Accepts 3 numbers (`f`, `e`, `h`).
* Adds them and stores the result in `k`.
* **Returns** the value of `k` to the calling code.

#### ✅ **Advantages:**

* You can **store** the result in a variable.
* You can **reuse** or **process** it further.
* You can **test** or **chain** this function.

#### 🔍 **Result:**

```python
Output: 11
```

---

