num = [1,2,3,4,5]

# for i in num:
#     # if i == 2:
    #     print('found')
    #     continue
    # print(i)
#     for letter in 'abc':
#         print(i ,letter)

# for i in range(4, 10):
#     print(i)
    
# for i in range(4, 10, 2):
#     print(i)

# for i in range(10):
#     print(i)
    
    
# for i in range(10, 0, -1):
#     print(i)


x = 0 

while(x < 10):
    if x == 5:
        break
            
print(x)
x += 1


| Topic                      | Syntax / Example                  | What it does                                      |
| -------------------------- | --------------------------------- | ------------------------------------------------- |
| `for` loop                 | `for i in num:`                   | Goes through each item in a sequence              |
| `if` inside loop           | `if i == 2:`                      | Checks a condition for each iteration             |
| `continue`                 | `continue`                        | Skips the current iteration and moves to the next |
| `break`                    | `break`                           | Immediately stops the loop                        |
| `range(stop)`              | `range(10)`                       | Generates `0` through `9`                         |
| `range(start, stop)`       | `range(4, 10)`                    | Generates `4` through `9`                         |
| `range(start, stop, step)` | `range(4, 10, 2)`                 | Generates `4, 6, 8`                               |
| Reverse `range`            | `range(10, 0, -1)`                | Generates `10` down to `1`                        |
| Loop through string        | `for letter in 'abc':`            | Iterates through each character                   |
| `while` loop               | `while x < 10:`                   | Repeats while condition is `True`                 |
| `break` in `while`         | `if x == 5: break`                | Stops the `while` loop when `x` reaches 5         |
| Loop variable              | `for i in num:`                   | `i` holds the current item                        |
| Nested loop                | `for i in ...` + `for j in ...`   | A loop inside another loop                        |
| `else` with loop           | `for ... else:`                   | Runs if loop finishes normally, without `break`   |
| `pass`                     | `pass`                            | Does nothing; placeholder                         |
| `enumerate()`              | `for i, value in enumerate(num):` | Gives both index and value                        |
| `zip()`                    | `for a, b in zip(x, y):`          | Loops through two sequences together              |
