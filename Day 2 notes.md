# 📘 Python Notes – Strings & Conditional Statements

Beginner-friendly notes covering:
- Strings in Python
- String Functions
- Conditional Statements
- Practice Programs

---

# 🔹 1️⃣ Strings in Python

## 📌 What is a String?

A **string** is a sequence of characters enclosed in quotes.

```python
name = "Santosh"
college = 'VTU'
```

Python supports:
- Single quotes `' '`
- Double quotes `" "`
- Triple quotes `''' '''` or `""" """`

---

## 📌 Indexing

```python
text = "Python"

print(text[0])   # P
print(text[3])   # h
```

### 🔹 Negative Indexing

```python
print(text[-1])  # n
print(text[-2])  # o
```

---

## 📌 Slicing

```python
text = "Python Programming"

print(text[0:6])    # Python
print(text[7:18])   # Programming
print(text[:6])     # Python
print(text[7:])     # Programming
```

---

## 📌 Strings are Immutable

Strings cannot be changed after creation.

```python
text = "Hello"
# text[0] = "h" ❌ Error
```

---

# 🔹 2️⃣ String Functions

## 📌 Case Conversion

```python
text = "python"

print(text.upper())      # PYTHON
print(text.lower())      # python
print(text.title())      # Python
print(text.capitalize()) # Python
```

---

## 📌 Removing Spaces

```python
text = "  hello  "

print(text.strip())      # Remove spaces from both sides
print(text.lstrip())     # Remove left space
print(text.rstrip())     # Remove right space
```

---

## 📌 Searching & Counting

```python
text = "Python Programming"

print(text.find("Pro"))   # Returns index
print(text.count("o"))    # Counts occurrences
```

---

## 📌 Replace

```python
text = "I love Java"

new_text = text.replace("Java", "Python")
print(new_text)
```

---

## 📌 Split & Join

```python
text = "apple,banana,mango"

fruits = text.split(",")
print(fruits)

joined = "-".join(fruits)
print(joined)
```

---

## 📌 Check Functions

```python
text = "Python123"

print(text.isalpha())        # False
print(text.isdigit())        # False
print(text.isalnum())        # True
print(text.startswith("Py")) # True
print(text.endswith("123"))  # True
```

---

# 🔹 3️⃣ Conditional Statements

Conditional statements are used to make decisions in programs.

---

## ✅ if Statement

```python
age = 18

if age >= 18:
    print("You are eligible to vote")
```

---

## ✅ if-else Statement

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## ✅ if-elif-else Statement

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

## ✅ Nested if

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
```

---

## ✅ Logical Operators

| Operator | Meaning |
|----------|----------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the condition |

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
```

---

# 🔥 Important Points

- Python uses indentation (4 spaces recommended).
- Strings are immutable.
- Use `==` for comparison, not `=`.
- Always maintain proper formatting.

---

# 📌 Practice Programs

## 1️⃣ Palindrome Check

```python
text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

## 2️⃣ Count Vowels

```python
text = input("Enter text: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)
```

---

## 3️⃣ Even or Odd

```python
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# 🚀 Author

Santosh Pujari  
CSE Student | Python Learner | Future Software Engineer 💻🔥
