# Project Roadmap

This document outlines the planned development direction for boxedLANG. It helps contributors understand future goals and guides feature prioritization.

## Vision

boxedLANG aims to be an accessible, educational programming language with a unique box-based paradigm. The long-term goal is to create a language that is:

- **Easy to learn**: Simple syntax suitable for beginners
- **Powerful**: Capable of solving real problems
- **Well-documented**: Comprehensive guides and examples
- **Community-driven**: Shaped by user feedback and contributions

## Roadmap Phases

### Phase 1: Foundation (Current - v0.1.x)

**Status**: In Progress

**Goals**:
- Core language features complete
- Stable interpreter implementation
- Comprehensive documentation
- Community establishment

**Completed**:
- Basic commands (say, box, ask, del)
- Control flow (jump, mark, jumpif)
- Arithmetic and conditionals
- Command-line interface
- Project documentation

**In Progress**:
- Contribution guidelines and processes
- Maintainer guides
- Architecture documentation

**Blockers**: None

### Phase 2: User Experience (v0.2.x)

**Status**: Planned

**Goals**:
- Improved error messages
- Better development tools
- More example programs
- Visual debugging tools

**Planned Features**:
- [ ] Error reporting with line numbers and context
- [ ] REPL (read-eval-print loop) mode
- [ ] Debugger with breakpoints
- [ ] Additional example programs
- [ ] Syntax highlighting for common editors
- [ ] Better variable inspection tools

**Estimated Timeline**: Q2-Q3 2025

### Phase 3: Advanced Features (v0.3.x)

**Status**: Proposed

**Goals**:
- Language enhancements
- Library/module system
- Performance optimization
- Testing framework

**Candidate Features**:
- [ ] String manipulation functions
- [ ] List/array support
- [ ] Function definitions and calls
- [ ] File I/O operations
- [ ] Module import system
- [ ] Built-in libraries
- [ ] Performance profiling tools

**Estimated Timeline**: Q4 2025 - Q1 2026

### Phase 4: Ecosystem (v1.0.x)

**Status**: Future

**Goals**:
- Official 1.0 release
- Package ecosystem
- Community contributions
- Stability and maintenance

**Planned Initiatives**:
- [ ] Package registry for shareware programs
- [ ] Official VSCode extension
- [ ] Web-based playground
- [ ] Community example collection
- [ ] Educational curriculum materials
- [ ] Official language specification

**Estimated Timeline**: 2026+

## Feature Requests Under Consideration

### High Priority
- **Better error messages**: Users report confusing errors; improving diagnostics would reduce support burden
- **REPL mode**: Interactive development would improve learning experience
- **Syntax highlighting**: Making the language more accessible to editors

### Medium Priority
- **String functions**: toUpper(), toLower(), concat(), substring()
- **List operations**: Support for arrays/lists in addition to boxes
- **File I/O**: Reading and writing files for data persistence
- **Comments**: // or # style comments in source code

### Low Priority
- **Function definitions**: Custom procedures and functions
- **Object-oriented features**: Classes and objects
- **Concurrency**: Parallel execution support
- **Compilation**: Compile to bytecode or native binaries

## Known Limitations

### Current Constraints

1. **Type System**: Everything is strings; no native numeric types
2. **Error Handling**: Minimal error reporting; confusing failures
3. **Performance**: No optimization; slow for large programs
4. **Scope**: Single global namespace; no variable scoping
5. **Testing**: Manual testing only; no automated test suite

### Future Improvements

- Implement proper type system with integers, floats, booleans
- Add comprehensive error handling and reporting
- Optimize execution engine for performance
- Introduce variable scoping and namespaces
- Create automated test framework

## Community Input

We actively seek community feedback on:

- **Feature priorities**: Which proposed features matter most?
- **Use cases**: How are you using boxedLANG? What's missing?
- **Pain points**: What makes development difficult?
- **Ideas**: What novel features would make boxedLANG better?

### How to Contribute to Roadmap

1. **Review this document** to understand planned direction
2. **Open an issue** with your feature idea or feedback
3. **Tag it appropriately**: feature-request, discussion, etc.
4. **Provide context**: Why is this important? How would you use it?
5. **Engage in discussion**: Help shape the future of boxedLANG

## Dependencies and Blockers

### Technical Dependencies

```
Better Error Messages
  └─ Requires: Line number tracking (Done)
  └─ Requires: Parser improvements (In Progress)

REPL Mode
  └─ Requires: Interactive execution (New)
  └─ Requires: State preservation (New)

File I/O
  └─ Requires: OS abstraction layer (New)
  └─ Requires: Error handling (Blocked: Phase 2)
```

### Known Blockers

- **Testing framework**: No automated tests; limits quality assurance
- **Type system**: String-only approach limits advanced features
- **Performance**: May block some real-world applications

## Success Metrics

We measure success through:

- **Community engagement**: Issues, PRs, discussions, stars
- **Project health**: Code quality, documentation completeness
- **User adoption**: Downloads, example programs, testimonials
- **Contribution velocity**: Regular submissions and activity

## Release Schedule

- **0.1.x**: Continuous maintenance and bug fixes
- **0.2.0**: Expected late 2025, focused on user experience
- **0.3.0**: Expected early 2026, advanced features
- **1.0.0**: Expected mid 2026, stable release

## How to Get Involved

1. **Review this roadmap** and comment on features you care about
2. **Check the Issues page** for current work
3. **Submit pull requests** that align with Phase 1-2 goals
4. **Help with documentation** and examples
5. **Test the interpreter** and report bugs

## Feedback and Questions

For roadmap questions or suggestions:

- Open a GitHub issue with `[ROADMAP]` prefix
- Start a discussion in GitHub Discussions
- Contact maintainers directly

We value your input in shaping the future of boxedLANG!

---

Last updated: February 2025
