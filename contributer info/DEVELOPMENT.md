# Development Guide for boxedLANG

This guide provides setup instructions and development information for contributors working on the boxedLANG Python runner.

## Development Environment Setup

### Prerequisites

- Python 3.8 or higher
- Git
- pip (Python package manager)

### Initial Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/mc20000-01/boxedLANG-py.git
   cd boxedLANG-py
   ```

2. Create a virtual environment (recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in editable mode:
   ```sh
   pip install -e .
   ```

   This installs boxedLANG with all dependencies and allows you to make changes without reinstalling.

4. Verify installation:
   ```sh
   boxrun boxcode/hello.bx
   ```

## Project Architecture

### Core Components

#### box_to_json.py
Responsible for parsing `.bx` source code into an intermediate JSON representation.

Key functions:
- `pull_cmd_from()` - Extracts command and arguments from a single line
- `make_code_from()` - Converts entire source code to JSON format
- `mk()` - Wrapper for code parsing
- `undo_mk()` - Converts JSON back to `.bx` format

#### box_runner.py
Executes the parsed JSON instructions and manages runtime state.

Key functions:
- `get_arg()` - Resolves variable substitution with `$` syntax
- `test()` - Evaluates conditional expressions
- `start_boxed_code()` - Main execution entry point

Key variables:
- `boxes` - Dictionary storing all named data containers
- `marks` - Dictionary storing labeled jump locations
- `l` - Current line number counter

#### main.py
Entry point that handles command-line argument parsing and file reading.

### Project Structure

```
boxedLANG-py/
├── boxrun/
│   ├── __init__.py         # Package initialization
│   ├── main.py             # CLI entry point
│   ├── box_runner.py       # Execution engine (144 lines)
│   ├── box_to_json.py      # Parser
│   └── box to py.py        # Utility functions
├── boxcode/
│   ├── hello.bx            # Hello World example
│   ├── test.bx             # Control flow example
│   ├── all_cmds.bx         # Command reference
│   ├── true.bx             # Boolean true example
│   └── false.bx            # Boolean false example
├── pyproject.toml          # Project metadata and dependencies
├── readme.md               # User documentation
├── CONTRIBUTING.md         # Contribution guidelines
├── DEVELOPMENT.md          # This file
└── CHANGELOG.md            # Version history (if applicable)
```

## Making Changes

### Adding a New Command

1. **Update the parser** in `box_to_json.py` if needed (only if command syntax is different)

2. **Implement the command** in `box_runner.py`:
   - Add a new case in the command-matching logic
   - Handle argument parsing with `get_arg()`
   - Implement the command logic
   - Update box state if needed

3. **Add examples** to `boxcode/all_cmds.bx` showing the command syntax

4. **Update documentation**:
   - Add to the Command Reference in `readme.md`
   - Include usage examples
   - Document any special behavior

5. **Test thoroughly**:
   - Create a `.bx` file that uses the new command
   - Test normal operation
   - Test edge cases
   - Test integration with existing commands

### Modifying Existing Functionality

1. Make your changes in the appropriate module
2. Update documentation if behavior changes
3. Test with existing example files to ensure backward compatibility
4. Create new examples if the modification adds new capability

## Testing

### Manual Testing

The primary testing method is manual execution with `.bx` files:

```sh
boxrun boxcode/hello.bx
boxrun boxcode/test.bx
```

### Creating Test Programs

Create new `.bx` files in `boxcode/` to test specific features:

1. **Unit-level tests**: Create files testing single commands
2. **Integration tests**: Create files testing command interactions
3. **Edge case tests**: Test boundary conditions and error scenarios

Example test file structure:
```
# Test file: boxcode/test_new_feature.bx
# Purpose: Verify new feature works correctly

say Testing~new~feature
# Test code here
say Test~complete
```

## Debugging

### Print Statements

Add `print()` statements in Python files to trace execution:

```python
def get_arg(argnumb, args, boxes):
    print(f"DEBUG: Getting arg {argnumb} from {args}")
    # ... rest of code
```

### Running with Debugging

Execute Python directly to see debug output:

```sh
python -m boxrun.main boxcode/hello.bx
```

### Checking Parsed Output

To see what your `.bx` code gets parsed to, you can temporarily modify a test file to print the JSON output.

## Dependencies

### Runtime Dependencies

- `colorama` - For colored terminal output

### Build System

- `setuptools` - For packaging and installation

All dependencies are specified in `pyproject.toml`.

## Version Management

Version is defined in `pyproject.toml`. When making significant changes, consider documenting them in a CHANGELOG.md file.

## Common Development Tasks

### Running the Interpreter

```sh
# Run a boxedLANG program
boxrun boxcode/hello.bx

# Run with Python directly (useful for debugging)
python -m boxrun.main boxcode/hello.bx
```

### Reinstalling After Changes

If you've modified setup-related files, reinstall in development mode:

```sh
pip install -e .
```

### Reviewing Changes

```sh
git diff                    # See unstaged changes
git diff --staged           # See staged changes
git status                  # See file status
```

## Code Review Checklist

Before submitting a pull request, verify:

- [ ] Code follows PEP 8 style guidelines
- [ ] Changes are focused and address a single issue
- [ ] Existing functionality is not broken
- [ ] New features are documented
- [ ] Example `.bx` files demonstrate the changes
- [ ] Commit messages are clear and descriptive
- [ ] No unnecessary dependencies were added

## Getting Help

If you encounter issues or have questions:

1. Check the README and existing documentation
2. Review existing issues and pull requests
3. Create a new issue with detailed information
4. Reach out to maintainers for guidance

## Additional Resources

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Documentation](https://docs.python.org/)
- boxedLANG README - See [readme.md](readme.md)

Happy contributing!
