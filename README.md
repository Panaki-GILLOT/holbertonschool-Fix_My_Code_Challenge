# holbertonschool-Fix_My_Code_Challenge

## Description

**Fix my code** is a new type of project, where we jump into an existing
code base and fix it!

Sometimes we know the language, sometimes not. The goal is not to recode
everything, just to find the bug(s) and fix them with minimal changes.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are compiled/interpreted on Ubuntu 20.04 LTS
- All files end with a new line

## Tasks

| # | Task | File | Language |
| --- | --- | --- | --- |
| 0 | FizzBuzz | [challenge/0-fizzbuzz.py](challenge/0-fizzbuzz.py) | Python |
| 1 | Print square | [challenge/1-print_square.js](challenge/1-print_square.js) | JavaScript |
| 2 | Sort | [challenge/2-sort.rb](challenge/2-sort.rb) | Ruby |

### 0. FizzBuzz

`0-fizzbuzz.py` prints numbers from 1 to `n`, replacing multiples of 3 with
`Fizz`, multiples of 5 with `Buzz`, and multiples of 15 with `FizzBuzz`.

**Bug:** the `if`/`elif` chain checked `i % 3` and `i % 5` before
`i % 15`, so the `FizzBuzz` branch was unreachable dead code.

**Fix:** check `i % 15 == 0` first.

### 1. Print square

`1-print_square.js` prints a square of `#` of a given size.

**Bug:** the size argument was parsed with `parseInt(process.argv[2], 16)`,
i.e. as hexadecimal instead of decimal, so `10` was read as `16`.

**Fix:** parse the argument with radix `10`.

### 2. Sort

`2-sort.rb` sorts the integer command line arguments in ascending order,
ignoring non-integer arguments.

**Bug:** the insertion step used `result.insert(i - 1, i_arg)`. When the
correct insertion index was `0`, `i - 1` became `-1`, and Ruby's
`Array#insert` treats a negative index as counting from the end, so the
value was appended instead of inserted at the front, scrambling the sort.

**Fix:** insert at `result.insert(i, i_arg)`.

## Author

Guillaume
