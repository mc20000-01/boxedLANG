# Architecture Overview

## System Design

boxedLANG follows a classic interpreter architecture with two main stages: parsing and execution.

```
┌─────────────────────────────────────────┐
│         boxedLANG Source Code           │
│              (.bx files)                │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│           Parser (box_to_json.py)       │
│  Converts ASCII syntax to JSON format   │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│       Intermediate JSON Representation  │
│  Each command becomes a JSON object     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│        Executor (box_runner.py)         │
│   Processes JSON and manages state      │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│         Program Output & Effects       │
│    (Console output, variable state)    │
└─────────────────────────────────────────┘
```

## Core Modules

### main.py - Entry Point

**Responsibility**: Command-line interface and file handling

**Key Operations**:
1. Accepts `.bx` file path from command line
2. Reads file contents
3. Passes code to executor
4. Returns exit status

**Dependencies**: `pathlib`, `sys`, `os.path`

### box_to_json.py - Parser

**Responsibility**: Syntax analysis and code transformation

**Data Flow**:
```
Raw source code
  │
  ├─→ split into lines
  │
  ├─→ for each line:
  │     ├─ extract command
  │     ├─ extract arguments (split by pipe |)
  │     ├─ check for marks
  │     └─ create JSON object
  │
  └─→ JSON array of commands
```

**Key Functions**:

- `pull_cmd_from(box_line, ln)` - Parse single line
  - Input: Source code line string
  - Output: Dictionary with `cmd`, `args`, `ln`, `marks`
  - Logic:
    - Split line by spaces to extract command
    - Handle `premark` directive for labels
    - Split final argument by `|` to get argument list

- `make_code_from(code)` - Parse entire program
  - Input: Multi-line source code string
  - Output: List of command JSON objects
  - Logic:
    - Split code into lines
    - Process each line with `pull_cmd_from()`
    - Prepend startup command to beginning

- `mk(code)` - Convenience wrapper
  - Calls `make_code_from()`
  - Used by executor

- `undo_mk(boxed_code)` - Reverse operation
  - Converts JSON back to `.bx` format
  - Used for debugging or code generation

**JSON Format**:
```json
{
  "cmd": "say",
  "args": ["hello", "world"],
  "ln": 0,
  "marks": {}
}
```

### box_runner.py - Executor

**Responsibility**: Program execution and runtime state management

**State Variables**:

- `boxes` (dict) - Stores all named data containers
  ```python
  boxes = {
    "name": "John",
    "age": "25",
    "count": "0"
  }
  ```

- `marks` (dict) - Stores labeled jump locations
  ```python
  marks = {
    "loop": 5,
    "start": 0
  }
  ```

- `l` (int) - Current instruction line number (initially -1)

**Execution Flow**:
```
Start
  │
  ├─→ Parse code to JSON
  │
  ├─→ Initialize state (boxes, marks, line counter)
  │
  ├─→ Main loop:
  │     ├─ Get current instruction
  │     ├─ Match command type
  │     ├─ Execute appropriate handler
  │     ├─ Update state (boxes, or jump)
  │     └─ Increment line counter (unless jumped)
  │
  └─→ End (when reach last instruction)
```

**Key Functions**:

- `get_arg(argnumb, args, boxes)` - Argument resolution
  - Handles variable substitution with `$` prefix
  - Replaces `~` with spaces
  - Removes `:` characters
  - Returns resolved string

- `test(arg1, arg2, op)` - Conditional evaluation
  - Supports operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Returns boolean result
  - Used by conditional commands

- `start_boxed_code(code, filename)` - Main executor
  - Takes raw source code string
  - Parses to JSON
  - Executes instructions in order
  - Handles all command dispatching

**Command Handler Pattern**:

Each command is handled within a `match` statement:
```python
match cmd:
    case "say":
        # Handle say command
        # Usage: say message|arg
    case "box":
        # Handle box command
        # Usage: box name|data
    # ... other cases
```

## Data Flow Examples

### Variable Substitution

**Source Code**:
```
box name|Alice
say hello~$name
```

**Execution**:
1. Command 1: `box name|Alice`
   - `boxes["name"] = "Alice"`

2. Command 2: `say hello~$name`
   - Input args: `["hello~$name"]`
   - `get_arg()` processes:
     - Finds `$name` → Looks up `boxes["name"]` → "Alice"
     - Replaces `~` with spaces
     - Result: "hello Alice"
   - Output: `hello Alice`

### Control Flow with Marks

**Source Code**:
```
mark loop
say counting
math counter|0|+|1
jumpif $counter|5|<|loop|m
```

**Execution Flow**:
1. Line 0: `mark loop`
   - `marks["loop"] = 0`
   - Continue

2. Line 1: `say counting`
   - Output: `counting`
   - Continue

3. Line 2: `math counter|0|+|1`
   - `boxes["counter"] = 1`
   - Continue

4. Line 3: `jumpif ...`
   - Evaluate: `1 < 5` → True
   - Jump to line referenced by `marks["loop"]` (which is 0)
   - Set `l = 0` (line counter)

5. Repeat from line 0...

## Syntax Conventions

### Delimiter Roles

- **Space** - Separates command from arguments
- **Pipe `|`** - Separates arguments from each other
- **Tilde `~`** - Represents spaces within arguments
- **Dollar `$`** - Marks variable references
- **Colon `:`** - Stripped during parsing (for formatting)

### Example Syntax Parsing

```
say hello~world|arg2|arg3
 │   └──────────┬────────┘
 │              └─ Split by pipes
 │
 └─ Command
```

Result:
- Command: `say`
- Args: `["hello~world", "arg2", "arg3"]`

## Error Handling

Currently, the interpreter has minimal error handling:

- **Missing boxes**: Returns empty string
- **Invalid operators**: May produce unexpected results
- **Index out of bounds**: Returns empty string or indexed value

Future improvements could include:
- Proper exception handling
- Informative error messages with line numbers
- Type checking for operations

## Performance Considerations

- **Linear scan**: Instructions processed sequentially
- **Dictionary lookup**: O(1) variable resolution
- **No optimization**: Code is interpreted as-is
- **String operations**: Frequent string concatenation could be optimized

## Extension Points

### Adding New Commands

1. Do not modify parser unless syntax is special
2. Add case in `start_boxed_code()` match statement
3. Use `get_arg()` for argument resolution
4. Update `boxes` dictionary for state changes
5. Handle jump by setting `l` variable

### Adding New Operators

Search for `match op:` in `test()` function and add new case.

### Adding New Data Types

Current system only uses strings. To support other types:
- Modify `boxes` to store mixed types
- Update `get_arg()` to handle type conversion
- Update operations to handle type-specific logic

## Dependencies

- **colorama**: For colored terminal output (used in error reporting)
- **setuptools**: For packaging (build-time only)

All dependencies are minimal to keep the project lightweight.

---

For more details on specific features, see [DEVELOPMENT.md](DEVELOPMENT.md).
