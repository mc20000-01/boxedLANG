# Testing Guide

This document describes testing procedures and best practices for boxedLANG.

## Testing Philosophy

boxedLANG uses manual integration testing supplemented by example programs. While automated unit tests are planned, the current approach focuses on ensuring example programs work correctly.

## Test Categories

### 1. Manual Integration Tests

**Purpose**: Verify that programs run correctly end-to-end

**Procedure**:
```sh
# Navigate to project root
cd /workspaces/boxedLANG-py

# Run example program
boxrun boxcode/hello.bx

# Verify output matches expected behavior
```

**Examples to test**:
- `hello.bx` - Basic input/output
- `test.bx` - Control flow and jumps
- `all_cmds.bx` - Command reference

### 2. Feature-Specific Tests

Create `.bx` files in `boxcode/` to test specific features:

**Structure**:
```
# File header with description
# Purpose: Test [feature name]
# Expected output: [what should print]

# Test code here
say Test~complete
```

**Example**: Testing the `math` command

**File**: `boxcode/test_math.bx`
```
# Test: Mathematical operations
# Purpose: Verify math command works correctly
# Expected: Should output results of arithmetic

say Starting~math~tests
math result|5|+|3
say 5~plus~3~equals:~$result
math result|10|-|4
say 10~minus~4~equals:~$result
say Tests~complete
```

**Run**:
```sh
boxrun boxcode/test_math.bx
```

### 3. Edge Case Testing

Test boundary conditions and unusual inputs:

**Variables to test**:
- Empty strings
- Special characters in variable names
- Large numbers
- Negative numbers
- Spaces in data

**Example**:
```
# Test: Edge cases in variable handling

box empty|
say Empty~box~value~is:~$empty
box special|!@#$%

box number|999999999
math large|$number|+|1
say Large~number~result:~$large

say Edge~case~tests~complete
```

### 4. Error Condition Testing

Test program behavior when things go wrong:

**Scenarios**:
- Jumping to non-existent marks
- Referencing undefined variables
- Invalid operators
- Malformed commands

**Example**:
```
# Test: Error handling

# Reference undefined variable
say Undefined~variable~is:~$undefined
# Expected: Should continue (returns empty string)

# Use invalid operator
test result|5|>>>|3|true|false
# Expected: Should handle gracefully or error

say Error~handling~test~complete
```

## Creating Test Programs

### Guidelines

1. **Clear Purpose**: Add comment header explaining what's tested
2. **Expected Output**: Document what correct output looks like
3. **Self-Contained**: Don't depend on other test files
4. **Comprehensive**: Test normal cases and edge cases
5. **Discoverable**: Use descriptive filenames like `test_*.bx`

### Template

```
# Test: [Feature Name]
# Purpose: Verify [specific functionality]
#
# Expected Output:
# [Describe what should print]
#
# Created: YYYY-MM-DD
# Modified: YYYY-MM-DD

# Initialization
box test_passed|yes

# Test code here

# Final verification
say Test~result:~$test_passed
```

## Testing Commands

### Testing Input/Output (`say`, `ask`)

```
# Test: Output with spacing and variables

box name|World
say hello~$name
say Sentences~can~have~multiple~words
```

### Testing Variables (`box`, `del`)

```
# Test: Variable management

box myvar|initial_value
say Original~value:~$myvar

box myvar|new_value
say Updated~value:~$myvar

del myvar
say After~deletion:~$myvar
```

### Testing Arithmetic (`math`)

```
# Test: Mathematical operations

math add|2|+|3
say 2~+~3~=~$add

math sub|10|-|4
say 10~-~4~=~$sub

math mul|6|*|7
say 6~*~7~=~$mul

math div|20|/|4
say 20~/~4~=~$div
```

### Testing Control Flow (`jump`, `mark`, `jumpif`)

```
# Test: Conditional jumps and loops

box counter|0

mark loop
say Loop~iteration:~$counter

math counter|$counter|+|1
test continue|$counter|5|<|loop|end
jump loop

mark end
say Loop~complete
```

### Testing Conditionals (`test`, `if`)

```
# Test: Conditional logic

test result|apple|apple|==|match|nomatch
if $result|match|match|say|Values~match
if $result|nomatch|nomatch|say|Values~dont~match
```

## Regression Testing

Before each release, run all test programs:

```sh
#!/bin/bash
# Script to run all test programs

cd boxcode

for test_file in *.bx; do
    echo "Testing: $test_file"
    boxrun "$test_file"
    echo "---"
done
```

**What to verify**:
- Programs complete without crashing
- Output matches expectations
- No unexpected errors

## Performance Testing

### Current Approach

Informal testing by running programs and observing execution time.

### Basic Performance Test

**File**: `boxcode/perf_test.bx`
```
# Test: Performance with loops

box counter|0

mark loop
math counter|$counter|+|1

test continue|$counter|1000|<|loop|end
jump loop

mark end
say Completed~1000~loop~iterations
```

**Run and time**:
```sh
time boxrun boxcode/perf_test.bx
```

### Performance Targets

- Small programs (<100 lines): <1 second
- Medium programs (100-1000 lines): <10 seconds
- Large programs (1000+ lines): <1 minute

## Compatibility Testing

### Python Versions

Test on minimum supported version (3.8):

```sh
# Using pyenv or similar
pyenv install 3.8.0
pyenv shell 3.8.0

pip install -e .
boxrun boxcode/hello.bx
```

### Operating Systems

Test on:
- Linux (primary development)
- macOS (using Darwin python)
- Windows (using Python.org or Windows Store)

**Critical features to test on all platforms**:
- File path handling
- Output formatting
- Input handling

## Continuous Integration (Future)

When implementing CI/CD:

```yaml
# Planned: GitHub Actions workflow

name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.8', '3.9', '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install
      run: pip install -e .
    - name: Run integration tests
      run: |
        boxrun boxcode/hello.bx
        boxrun boxcode/test.bx
```

## Reporting Test Results

### Format for Issue Reports

```markdown
### Test Results

**Program**: boxcode/hello.bx
**Python Version**: 3.9
**OS**: Ubuntu 22.04
**Status**: PASS / FAIL

**Expected Output**:
```
hello world
```

**Actual Output**:
```
[actual output here]
```

**Notes**:
- Any additional observations
```

## Debugging Failed Tests

### Enable Debug Output

Temporarily add print statements to `boxrun/box_runner.py`:

```python
def start_boxed_code(code, filename):
    print(f"DEBUG: Starting execution of {filename}")
    print(f"DEBUG: Code length: {len(code)} characters")
    # ... rest of code
```

### Trace Execution

```python
# In main loop
print(f"DEBUG: Line {l}, Command: {cmd}, Args: {args}")
print(f"DEBUG: Boxes state: {boxes}")
```

### Check Parsed Code

Add temporary debugging to see JSON parse result:

```python
parsed = mk(CODE)
print("DEBUG: Parsed code:")
for instruction in parsed:
    print(instruction)
```

## Test Documentation

When creating tests, document:

1. **What**: What feature is being tested?
2. **Why**: Why is this test important?
3. **How**: Step-by-step execution
4. **Expected**: What should happen?
5. **Actual**: What actually happened (for failed tests)

## Best Practices

1. **Isolate Tests**: Each test file should test one primary feature
2. **Clear Names**: Use descriptive filenames like `test_command_name.bx`
3. **Verify Output**: Compare actual vs expected carefully
4. **Document Failures**: Keep notes on what breaks during development
5. **Repeatable**: Ensure tests can be run multiple times with same results
6. **Automated Validation**: Where possible, validate output automatically

## Common Issues and Solutions

### Output Not Matching

**Issue**: Program runs but output differs from expected

**Solution**:
1. Check for whitespace differences
2. Verify variable substitution works
3. Check for typos in assertions

### Program Crashes

**Issue**: boxrun exits with error

**Solution**:
1. Run with Python directly: `python -m boxrun.main file.bx`
2. Add debug print statements
3. Verify syntax in `.bx` file

### Hanging Programs

**Issue**: Program never completes

**Solution**:
1. Check for infinite loops
2. Verify jump targets exist
3. Check mark definitions

## Future Testing Improvements

Planned enhancements:

- [ ] Automated unit tests for parser and executor
- [ ] Test framework for `.bx` programs
- [ ] Continuous integration setup
- [ ] Code coverage reporting
- [ ] Performance benchmarking
- [ ] Formal test suite

---

For questions about testing, see DEVELOPMENT.md or open an issue.
