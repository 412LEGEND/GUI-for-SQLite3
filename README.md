# GUI-for-SQLite3
A simple GUI for SQLite3, written in Python.

## Prerequisites
You need to have Python 3 and SQLite3 installed correctly.

## Instructions

### 1. Connecting a database

When you open the program a terminal window will come up to you. Enter the path to the database. If it doesn't exist the program will create a new onw.

### 2. Customizing the style of the output

The next line you'll have to enter is the style of the input.

#### Built-in styles

- separation_comma: List `[a, b, c, ...]` will be `a,b,c,...`

- separation_space: List `[a, b, c, ...]` will be `a b c,...`

- separation_semi: List `[a, b, c, ...]` will be `a; b; c,...`

- order_num: Ordered list, e.g. `0: a; 1: b; ...`

- order_hex: Hexadecimal. E.g. `0x00:a; 0x01:b; 0x02:c;...`

- order_alnum: Alphanumerical. E.g. `0: 0; ...; a: 11; b: 12; ...; z: 36; 0: 37; ...`

#### User-defined

The program supports user-defined styles.

##### Way #1

- The style `\sep`: `[a, b, c]` will be `asepbsepcsep`.
  - For example, `\ - `: `[a, b, c]` --> `a - b - c - `.

##### Way #2

- Use `${n}` to present `list[n]`.
  - For example, `First: $${0}; Second: $${1}; Total: $${2}.`: `[10, 23, 33]` --> `First: $10; Second: $23; Total: $33.`.

##### Shorthand for Way #2

- Use `:pat1 pat2 pat3 pat4 ... patn` to present `pat1: ${0}; pat2: ${1}; pat3: ${2}; ...; patn: ${n-1}; pat1: ${n}; pat2: ${n+1}; ...`.
  - For example, `:a b c`: `[1, 2, 3, 4, 5]` --> `a: 1; b: 2; c: 3; a: 4; b: 5;`


### 3. Executing and committing

Enter SQL commands in the entry, execute by clicking the button "Execute command", clear the entry by clicking "Clear input".
Every changes you made will save automatically.

### 4. Enjoy!
