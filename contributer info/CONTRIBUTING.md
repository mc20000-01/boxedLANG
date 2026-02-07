# Contributing to boxedLANG

Thank you for your interest in contributing to boxedLANG! This document outlines how to contribute to the project.

## Code of Conduct

This project is committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

If you discover a bug, please open an issue on GitHub with:

- A clear, descriptive title
- A detailed description of the bug
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Your environment (Python version, OS)
- Sample code or `.bx` file that demonstrates the problem

### Suggesting Features

To suggest a new feature:

- Open an issue with the title prefixed by `[FEATURE]`
- Describe the proposed feature and its use case
- Explain why you believe this feature would be valuable
- Provide examples of how the feature would be used

### Submitting Changes

1. **Fork the repository** on GitHub
2. **Create a branch** for your changes:
   ```sh
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```
3. **Make your changes** following the coding standards (see below)
4. **Test your changes** thoroughly
5. **Commit with clear messages**:
   ```sh
   git commit -m "Add descriptive commit message"
   ```
6. **Push to your fork**:
   ```sh
   git push origin your-branch-name
   ```
7. **Open a Pull Request** on the main repository with:
   - A clear description of the changes
   - Reference to any related issues
   - Explanation of how to test the changes

## Development Setup

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed development environment setup instructions.

## Coding Standards

### Python Code

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Aim for code clarity over brevity

### boxedLANG Code Examples

- Use clear, well-commented examples
- Follow the syntax documented in the README
- Test all example code before committing

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Keep the first line to 50 characters or less
- Provide additional context in the message body if needed

Example:
```
Add jump command with mark support

Implement the jump command that allows programs to jump to
a specified line or labeled mark. Includes support for
conditional jumps based on premark locations.
```

## Testing

Before submitting a pull request:

1. Test your changes manually with appropriate `.bx` files
2. Verify existing functionality still works
3. Test edge cases and error conditions
4. Update or create example programs that demonstrate your changes

## Documentation

- Update the README if your changes affect user-facing functionality
- Update DEVELOPMENT.md if your changes affect the development process
- Add inline comments for complex logic
- Document new commands or features with examples

## Pull Request Process

1. Ensure your code follows the coding standards
2. Update documentation as needed
3. Provide a clear description of what your PR does
4. Be open to feedback and requests for changes
5. Ensure your PR is against the main branch

## Areas for Contribution

- **Bug fixes**: Resolve reported issues
- **Feature implementation**: Add new language features or commands
- **Documentation**: Improve README, code comments, and guides
- **Examples**: Create example programs demonstrating features
- **Testing**: Expand test coverage and edge case testing
- **Performance**: Optimize the interpreter or parser

## Questions?

If you have questions about contributing, please open a discussion issue or reach out to the maintainers.

We appreciate your contributions!
