

# boxedLANG Python runner

An interpreted programming language with a box-based paradigm. boxedLANG provides a simple, command-driven syntax for writing programs that manage data in named containers called boxes.

## Overview

boxedLANG is a lightweight scripting language made by jamie designed for educational purposes and simple automation tasks. Programs are written in files with a `.bx` extension and executed through the boxrun interpreter.

## Installation

### Prerequisites

- Python 3.8 or higher

### Setup

```sh
git clone https://github.com/mc20000-01/boxedLANG.git
cd boxedLANG-py
pip install -e .
```

## Usage

Run a boxedLANG program file:

```sh
boxrun path/to/program.bx
```

## Language Syntax

### Basic Concepts

- **Boxes**: Named containers that store data
- **Commands**: Actions that manipulate boxes and produce output
- **Variables**: Referenced with `$` prefix
- **Spaces**: Represented with `~` in arguments
- **Arguments**: Separated by pipe characters `|`

### Command Reference

#### Input/Output

- `say` - Output text to console
  ```
  say hello,~world!|0
  say message|time
  ```

- `ask` - Request user input and store in a box
  ```
  ask what~is~your~name
  ```

#### Data Management

- `box` - Create a new box and assign data
  ```
  box name|data
  ```

- `del` - Delete a box
  ```
  del name
  ```

#### Control Flow

- `jump` - Jump to a line or labeled mark
  ```
  jump test|m
  jump 5
  ```

- `mark` - Create a labeled marker at current line
  ```
  mark test
  ```

- `premark` - mark a location for jumping before any commands run (note premarks can be over written by any type of mark)
  ```
  premark test
  ```

- `jumpif` - Conditionally jump based on comparison
  ```
  jumpif data1|data2|==|label|ismark
  ```

#### Conditionals and Operations

- `test` - Test a condition (returns true/false)
  ```
  test boxname|data1|data2|op|iftrue|iffalse
  ```

- `if` - Execute commands conditionally
  ```
  if data1|data2|op|cmd|arg1|arg2|arg3
  ```

#### Arithmetic

- `math` - Perform mathematical operations
  ```
  math boxname|number1|+|number2
  ```

#### Timing

- `wait` - Pause execution for specified milliseconds
  ```
  wait 1000
  ```

### Variable Substitution

Use `$` to reference box values in commands:

```
box name|John
say hello~$name
```

### Example Programs

**Hello World**
```
say hello,~world!
ask what~is~your~name
say hello~$name
```

**Control Flow**
```
mark test
say worked|1
jump test
say did~not~work|1
premark test
```

## Project Structure

```
boxedLANG-py/
├── boxrun/                 # Interpreter implementation
│   ├── main.py            # Entry point
│   ├── box_runner.py      # Execution engine
│   ├── box_to_json.py     # Code parser
│   └── __init__.py
├── boxcode/               # Example programs
│   ├── hello.bx
│   ├── test.bx
│   ├── all_cmds.bx
│   ├── true.bx
│   └── false.bx
├── pyproject.toml         # Project configuration
└── readme.md
```

## Development

The interpreter works in two stages:

1. **Parsing**: The `box_to_json.py` module converts `.bx` source code into an intermediate JSON representation
2. **Execution**: The `box_runner.py` module executes the parsed instructions, managing boxes and executing commands

## License

See project repository for license information.
