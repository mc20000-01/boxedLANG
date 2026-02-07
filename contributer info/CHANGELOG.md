# Changelog

All notable changes to the boxedLANG project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup and documentation
- Core interpreter implementation
- Box-based programming paradigm
- Command reference and documentation
- Contributing guidelines

### Changed

### Deprecated

### Removed

### Fixed

### Security

---

## [0.1.0] - 2025-02-06

### Added
- Initial release of boxedLANG interpreter
- Core language features:
  - `box` command for variable assignment
  - `say` command for output
  - `ask` command for input
  - `del` command for variable deletion
  - `math` command for arithmetic operations
  - `test` command for conditional logic
  - `jump` command for control flow
  - `mark` and `premark` for jump labels
  - `jumpif` for conditional jumps
  - `if` for inline conditionals
  - `wait` command for delays
- Variable substitution with `$` syntax
- Example programs (hello.bx, test.bx)
- Comprehensive README with syntax documentation
- Basic project structure and packaging

---

## Guidelines for Maintainers

When releasing a new version:

1. Update the version number in `pyproject.toml`
2. Create a new section in this file with the release date
3. Document all changes in the appropriate category:
   - **Added**: New features
   - **Changed**: Modifications to existing features
   - **Deprecated**: Features scheduled for removal
   - **Removed**: Deleted features
   - **Fixed**: Bug fixes
   - **Security**: Security-related fixes

4. Create a git tag with the version number:
   ```sh
   git tag -a v0.1.0 -m "Release version 0.1.0"
   git push origin v0.1.0
   ```

5. Update the unreleased section with new categories ready for the next release

### Example Entry Format

```markdown
### Added
- New command: `repeat` for looping with a counter
- Support for command aliases
- Colorized output for error messages

### Fixed
- Incorrect variable resolution when names contain special characters
- Memory leak in mark storage system

### Changed
- Improved error messages with line numbers
```

## Version History Reference

For a quick overview of notable changes:

- **0.1.0**: Initial release with core language features
