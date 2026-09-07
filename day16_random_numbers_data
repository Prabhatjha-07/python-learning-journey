import random

# value = random.random()
# print(value)

# value = random.uniform(1,20)
# print(value)

# value = random.randint(1,20)
# print(value)

# value = random.randrange(1,20,2)
# print(value)

# greetings = ["Hello", "Hi", "Hey", "Howdy", "Hola"]
# value = random.choice(greetings)
# print(value + " prabhat")

# colours = ["Red", "Blue", "Green", "Yellow", "Black"]
# value = random.choices(colours, k=3)
# value = random.choices(colours, weights=[18, 5, 3, 10, 1], k=3)
# print(value)

# deck = list(range(1, 52))
# random.shuffle(deck)
# hand = random.sample(deck, k=5)
# print(hand)
# print(deck)



# Day 16 — Python `random` Module

The `random` module is used to generate random numbers and select random items.

```python
import random
```

## 1. `random.random()`

Returns a random floating-point number between **0.0 and 1.0**.

```python
value = random.random()
print(value)
```

Example output:

```text
0.73452
```

---

## 2. `random.uniform(a, b)`

Returns a random **float** between `a` and `b`.

```python
value = random.uniform(1, 20)
print(value)
```

Example:

```text
13.472
```

---

## 3. `random.randint(a, b)`

Returns a random **integer**, including both `a` and `b`.

```python
value = random.randint(1, 20)
print(value)
```

Possible values:

```text
1, 2, 3, ..., 19, 20
```

---

## 4. `random.randrange(start, stop, step)`

Returns a random number from a range.

**Important:** `stop` is excluded.

```python
value = random.randrange(1, 20, 2)
print(value)
```

Possible values:

```text
1, 3, 5, 7, ..., 17, 19
```

---

## 5. `random.choice()`

Selects **one random item** from a sequence.

```python
greetings = ["Hello", "Hi", "Hey", "Howdy", "Hola"]

value = random.choice(greetings)
print(value)
```

---

## 6. `random.choices()`

Selects **multiple random items**.

```python
colours = ["Red", "Blue", "Green", "Yellow", "Black"]

value = random.choices(colours, k=3)
print(value)
```

Items **can be repeated**.

### Using weights

`weights` controls how likely each item is to be selected.

```python
value = random.choices(
    colours,
    weights=[18, 5, 3, 10, 1],
    k=3
)
```

Higher weight → higher probability.

---

## 7. `random.shuffle()`

Randomly rearranges the items in a list **in place**.

```python
deck = list(range(1, 52))

random.shuffle(deck)

print(deck)
```

`shuffle()` changes the original list and does **not** return a new list.

---

## 8. `random.sample()`

Selects multiple **unique** items from a sequence.

```python
hand = random.sample(deck, k=5)
print(hand)
```

`sample()` does not modify the original list.

**Important:** `k` cannot be greater than the number of available items.

---

## Quick Summary

| Function        | Purpose                                   |
| --------------- | ----------------------------------------- |
| `random()`      | Random float from `0.0` to `< 1.0`        |
| `uniform(a, b)` | Random float between `a` and `b`          |
| `randint(a, b)` | Random integer, both endpoints included   |
| `randrange()`   | Random value from a range, stop excluded  |
| `choice()`      | Select one random item                    |
| `choices()`     | Select multiple items, repetition allowed |
| `shuffle()`     | Shuffle a list in place                   |
| `sample()`      | Select multiple unique items              |

## Important Difference

```python
random.choice(list)
```

→ One item

```python
random.choices(list, k=3)
```

→ Multiple items, **repetition allowed**

```python
random.sample(list, k=3)
```

→ Multiple items, **no repetition**

```python
random.shuffle(list)
```

→ Rearranges the **original list**

## Extra: `random.seed()`

Use `seed()` when you want the same random results every time.

```python
random.seed(42)

print(random.randint(1, 10))
```

Using the same seed produces the same sequence of random values, which is useful for testing and debugging.
